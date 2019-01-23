from Crypto.Hash import SHA256
import hashlib

with open('1.3.1_input_string.txt') as f:
    input_string = f.read().strip()
with open('1.3.1_perturbed_string.txt') as f:
    perturbed_string = f.read().strip()

h1 = hashlib.sha256(input_string)
string1=h1.hexdigest()
print string1
h2 = hashlib.sha256(perturbed_string)
string2=h2.hexdigest()
print string2
counter = 0
for i in range(0, len(string1)):
    if string1[i]!=string2[i]:
        counter+=1
print counter
out_file = open('sol_1.3.1.hex', 'w')
out_file.write(str(counter).encode('hex'))
out_file.close()
