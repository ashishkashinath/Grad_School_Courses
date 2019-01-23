from Crypto.Cipher import AES

with open('1.2.3_aes_weak_ciphertext.hex') as f:
    file_content = f.read().strip()
ciphertext = file_content.decode('hex')
with open('sol_1.2.3.hex') as f:
    file_content = f.read().strip()
keytext = file_content.decode('hex')
iv = "00000000000000000000000000000000".decode('hex')
cipher_test=AES.new(keytext, AES.MODE_CBC, iv)
text_test = cipher_test.decrypt(ciphertext)
print text_test
for a in range(0,32) :
    key_text = chr(a).encode('hex').zfill(64)
    print key_text
    key = key_text.decode('hex')
    cipher=AES.new(key, AES.MODE_CBC, iv)
    text = cipher.decrypt(ciphertext)
    print text
