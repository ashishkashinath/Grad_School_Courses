from Crypto.PublicKey import RSA

with open('1.2.4_private_key.hex') as f:
    file_content = f.read().strip()
private_key = int(file_content,16)
print private_key
with open('1.2.4_RSA_modulo.hex') as f1:
    file_content1 = f1.read().strip()
modulo = int(file_content1,16)
with open('1.2.4_RSA_ciphertext.hex') as f2:
    file_content2 = f2.read().strip()
ciphertext = int(file_content2,16)

text=pow(ciphertext,private_key,modulo)
print int(text)
print hex(text)
