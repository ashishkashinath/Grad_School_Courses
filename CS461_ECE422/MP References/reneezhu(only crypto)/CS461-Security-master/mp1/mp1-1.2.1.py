with open("1.2.1_sub_key.txt") as f:
    file_content = f.read().strip()
print len(file_content)
text_map={}
for i in range(len(file_content)):
    text_map[file_content[i]] = chr(65+i)
print text_map
    
with open("1.2.1_sub_ciphertext.txt") as f2:
    file_content2 = f2.read().strip()
new_text = ""
for j in range(len(file_content2)):
    try:
        new_text+=text_map[file_content2[j]]
    except KeyError:
        new_text+=file_content2[j]
print new_text

sol_file = open('sol_1.2.1.txt', 'w')
sol_file.write(new_text)
sol_file.closed
