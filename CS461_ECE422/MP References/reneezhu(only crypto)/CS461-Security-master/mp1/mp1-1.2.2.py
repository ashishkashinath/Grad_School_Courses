from Crypto.Cipher import AES

with open('1.2.2_aes_key.hex') as f:
    file_content = f.read().strip()
key = file_content.decode('hex')
with open('1.2.2_aes_iv.hex') as f:
    file_content = f.read().strip()
iv = file_content.decode('hex')
with open('1.2.2_aes_ciphertext.hex') as f:
    file_content = f.read().strip()
ciphertext = file_content.decode('hex')
cipher = AES.new(key, AES.MODE_CBC,iv)
msg = cipher.decrypt(ciphertext)
out_f = open('sol_1.2.2.txt','r+')
out_f.write(str(msg))
out_f.closed
