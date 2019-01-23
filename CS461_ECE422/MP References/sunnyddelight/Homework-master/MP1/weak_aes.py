__author__ = 'Sunny'
import base64
import array
from Crypto.Cipher import AES
key='00000000000000000000000000000000000000000000000000000000000000'
iv='00000000000000000000000000000000'.decode("hex")
text='eb90325186b099e4591cd5b97d744dfc2d3d389dd30f80cbf9e72d327705217a391938a8d650d78b74ace564c3e353cfad6ea0243b5eb940859299e21463fa519848b6123f1519983efb2e86a2e8b62176eddc65efe503c9a529e70742cfbeb2bb37e2cf197691a8f74f3af7692b9a2b'.decode("hex")
mode=AES.MODE_CBC
for i in range(0,32):
    tempkey=key
    if i>15:
        tempkey+='1'
    else:
        tempkey+='0'

    if i%16>9:
        tempkey+=chr(i%16-10+ord('a'))
    else:
        tempkey+=str(i%16)
    print tempkey
    decryptor=AES.new(tempkey.decode('hex'),mode,iv)
    print decryptor.decrypt(text), '\n'
