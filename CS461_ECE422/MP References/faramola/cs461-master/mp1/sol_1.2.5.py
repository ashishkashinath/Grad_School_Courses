import string
import ipdb
import mp1_certbuilder
from Crypto.Util import number
from cryptography.hazmat.primitives.serialization import Encoding
import pymd5
import gmpy

def make_cert():
    while True:
        try:
            netid = 'fisiaka2'
            p = number.getPrime(1024)
            q = number.getPrime(1024)
            assert(p.bit_length() == 1024)
            assert(q.bit_length() == 1024)
            assert((p*q).bit_length() == 2047)
            privkey, pubkey = mp1_certbuilder.make_privkey(p, q)
            cert = mp1_certbuilder.make_cert(netid, pubkey)
            print(cert)
            return cert
        except AssertionError:
            continue

def save_cert(cert):
    with open('sol_1.2.5_certA.cer', 'wb') as f:
        f.write(cert.public_bytes(Encoding.DER))

def prefix(cert):
    while True:
        try:
            unused_idx = cert.tbs_certificate_bytes.find(''.join(map(chr, [117,110,117,115, 101, 100])))
            moduli_idx = cert.tbs_certificate_bytes.find(''.join(map(chr, [01, 00]))) + 2
            print moduli_idx
            tmp = cert.tbs_certificate_bytes[:unused_idx] + ''.join(['a'] * (64 - moduli_idx % 64)) + cert.tbs_certificate_bytes[unused_idx:moduli_idx]
            moduli_idx = tmp.find(''.join(map(chr, [01, 00])))
            assert len(tmp) % 64 == 0
            return tmp
        except AssertionError:
            continue

def cert_file_to_int(cert_str):
    # return cert_str.decode('hex')
    hex_str = ['{:02x}'.format(ord(c)) for c in cert_str]
    return int(''.join(hex_str), 16)

def get_md5_files():
    with open('certA1', 'r') as fp:
        md1 = fp.read()
    md1_idx = md1.find(''.join(map(chr, [01, 00]))) + 2
    bitStringOne = md1[md1_idx:]
    print len(bitStringOne)
    with open('certB2', 'r') as fp:
        md2 = fp.read()
    md2_idx = md2.find(''.join(map(chr, [01, 00]))) + 2
    bitStringTwo = md2[md2_idx:]
    assert len(bitStringOne) == 128
    assert len(bitStringTwo) == 128
    b1 = cert_file_to_int(bitStringOne)
    b2 = cert_file_to_int(bitStringTwo)
    print(b1.bit_length())
    print(b2.bit_length())
    # ipdb.set_trace()
    # currently 1024, need to check at OH
    # assert b1.bit_length() == 1023
    # assert b2.bit_length() == 1023
    b1 = b1 << 1024
    b2 = b2 << 1024
    assert (b1 % (2 ** 1024) == 0)
    assert (b2 % (2 ** 1024) == 0)
    return b1, b2

def gcd(a, b):
    """
    Algorithm from: https://en.wikipedia.org/wiki/Euclidean_algorithm
    returns the gcd for a and b
    :param a: value 1
    :param b: value 2
    :return: return the gcd between a and b
    """
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def get_p_values(b1, b2):
    p1 = number.getPrime(450)
    p2 = number.getPrime(450)
    N = p1*p2
    z1 = number.inverse(p2, p1)
    z2 = number.inverse(p1, p2)
    b0 = -(b1*p2*z1 + b2*p1*z2) %N
    # b0 = 0
    assert p1.bit_length() > 256
    assert p2.bit_length() > 256
    assert p1 != p2
    assert gcd(p1, p2) == 1
    assert gcd(p1-1, 65537) == 1
    assert gcd(p2-1, 65537) == 1
    assert (b1 + b0) % p1 == 0
    assert gcd(b1 + b0, p1) == p1
    assert gcd(b2 + b0, p2) == p2
    assert (b2 + b0) % p2 == 0.
    return (b0, p1, p2)

def get_q_values(b0, b1, b2, p1, p2):
    k = 0
    N = p1*p2
    print b0.bit_length()
    while True:
        try:
            if k % 100000 == 0:
                print 'k = ' + str(k)
            b = b0 + k*N
            if b > 2 ** 1024:
                raise ValueError('b has become too large.')
            q1 = (b1 + b)/p1
            assert q1.bit_length() > 256
            assert gcd(q1-1, 65537) == 1
            if not number.isPrime(q1):
                raise AssertionError
            n1 = b1 + b

            assert n1.bit_length() >= 2047
            # if n1.bit_length() > 2047:
            #     raise ValueError('n1 has become too large.')
            assert n1 != q1*p1
            break
        except AssertionError:
            k += 1
    print 'found p!'
    k = 0
    while True:
        try:
            if k % 100000 == 0:
                print 'k = ' + str(k)
            b = b0 + k * N
            if b > 2 ** 1024:
                raise ValueError('b has become too large.')
            q2 = (b2 + b)/p2
            assert q2.bit_length() > 256
            assert gcd(q2 - 1, 65537) == 1
            if not number.isPrime(q2):
                raise AssertionError
            n2 = b2 + b
            assert n2.bit_length() >= 2047
            assert n2 != q2*p2
            break
        except AssertionError:
            k+=1
    print 'found q!'
    return (q1, q2, b, n1, n2)

def create_privKeys(p1, q1, p2, q2):
    privkey_1, pubkey1 = mp1_certbuilder.make_privkey(p1, q1)
    privkey_2, pubkey2 = mp1_certbuilder.make_privkey(q2, p2)
    netid = 'fisiaka2'
    cert1 = mp1_certbuilder.make_cert(netid, pubkey1)
    cert2 = mp1_certbuilder.make_cert(netid, pubkey2)
    print(cert1)
    print(cert2)
    with open('sol_1.2.5_certA.cer', 'wb') as f:
        f.write(cert1.public_bytes(Encoding.DER))
    with open('sol_1.2.5_certB.cer', 'wb') as f:
        f.write(cert2.public_bytes(Encoding.DER))
    with open('sol_1.2.5_factorsA.hex', 'wb') as f:
        f.write(str(hex(p1)) + '\n')
        f.write(str(hex(q1)))
    with open('sol_1.2.5_factorsB.hex', 'wb') as f:
        f.write(str(hex(p2)) + '\n')
        f.write(str(hex(q2)))
    return cert1, cert2

if __name__ == '__main__':
    # cert = make_cert()
    # prefix = prefix(cert)
    # with open('prefix', 'w') as fp:
    #     fp.write(prefix)
    # print(prefix)
    b1, b2 = get_md5_files()
    b0, p1, p2 = get_p_values(b1, b2)
    q1, q2, b, n1, n2 = get_q_values(b0, b1, b2, p1, p2)
    with open('b_values1.2.5', 'w') as fp:
        fp.write('b0_' + str(b0) + '\n')
        fp.write('b1_' + str(b1) + '\n')
        fp.write('b2_' + str(b2) + '\n')
        fp.write('p1_' + str(p1) + '\n')
        fp.write('p2_' + str(p2) + '\n')
        fp.write('q1_' + str(q1) + '\n')
        fp.write('q2_' + str(q2) + '\n')
        fp.write('b_' + str(b) + '\n')
        fp.write('n1_' + str(n1) + '\n')
        fp.write('n2_' + str(n2) + '\n')
    create_privKeys(p1, q1, p2, q2)
