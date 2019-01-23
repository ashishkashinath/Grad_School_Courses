__author__ = 'duansy'

def WHA(inStr):
    mask=0x3fffffff
    outHash=0
    for letter in inStr:
        byte= ord(letter)
        iv=((byte^0xCC) <<24) | ((byte^0x33)<<16) | ((byte^0xAA)<<8 ) | (byte ^ 0x55)
        outHash=outHash&mask
        outHash+=iv&mask
    print hex(outHash)
WHA("HOLY MOSES  HE PLAYED A DOCTOR FIGHTING OFF ZOMBIES SPAWNED BY GERM WARFARE IN THE OMEGA MNA")