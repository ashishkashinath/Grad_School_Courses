import numpy as np
import Crypto.PublicKey.RSA
from Crypto.Util.number import inverse
import pbp

def get_rsa_values():
    """
    Reads from the 1.2.4.moduli.hex which is the same file as https://subversion.ews.illinois.edu/svn/fa17-cs461/_shared/mp1/moduli.hex
    :return: a list of long values in the moduli file
    """
    result = []
    with open('1.2.4.moduli.hex', 'r') as fp:
        for line in fp:
            result.append(int(line.strip(), 16))
    return result

def gcd_find_alg(values):
    """
    numpy implementation of the quasilinear GCD algorithm as described in 
    https://factorable.net/weakkeys12.extended.pdf
    :param values: values to apply the GCD algorithm
    :return: the gcd between the product of all of the values and each index in input values. If value
    is 1 at idx, the values[idx] is relative prime to every other value in values. 
    """
    np_val = np.array(values)
    p = np.prod(np_val)
    print('p = {}'.format(str(p)))
    values_squared = np_val ** 2
    z = np.remainder(p, values_squared)
    return [gcd(v, z[idx]/v) for idx, v in enumerate(values)]

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

def decrypt(modulus, gcd_values, c):
    """
    Decrypt cyphertext
    :param modulus: moduli from modulus file
    :param gcd_values: computed GCD values of modulus from gcd_find_alg
    :param c: str cyphertext
    :return: Decrypted string. None if can't find anything
    """
    exp = 65537
    for idx in range(len(gcd_values)):
        if(gcd_values[idx] == 1):
            continue
        d = inverse(exp, (gcd_values[idx]-1)*(modulus[idx]/gcd_values[idx]-1))
        rsakey = Crypto.PublicKey.RSA.construct((long(modulus[idx]), long(exp), long(d),long(gcd_values[idx])))
        try:
            return pbp.decrypt(rsakey, c)
        except ValueError:
            pass

if __name__ == '__main__':
    # rsa_values = get_rsa_values()
    # gcd_values = gcd_find_alg(rsa_values)
    # with open('gcd_values', 'w') as fp:
    #     for v in gcd_values:
    #         fp.write(str(v) + '\n')
    gcd_values = []
    rsa_key = None
    # read moduli file
    modulus = get_rsa_values()
    # read computed result by applying the quasilinear GCD function
    with open('gcd_values', 'r') as fp:
        for line in fp:
            gcd_values.append(int(line.strip()))

    # read ciphertext
    with open('1.2.4_ciphertext.enc.asc', 'r') as fp:
        # rsa_key = RSA.importKey(fp.read())
        c = fp.read()

    print(decrypt(modulus, gcd_values, c))
