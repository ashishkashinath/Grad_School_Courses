__author__ = 'Sunny'
def decrypt_sub(key,cipher):
    cur=0
    encryption={}
    output=''
    j=0
    for i in range(0,26):
        encryption[key[i]]=chr(i+ord('A'))
    for letter in cipher:
        if letter<'A' or letter > 'Z':
            output+=letter
        else:
            output+=encryption[letter]
    print output
decrypt_sub('UJPMCZSALBKYNQFGOXVWHTIRDE','WALV 8YCWWCX IFXM ZFX U PFYYCPWLFQ FZ JYFFM HVHUYYD PYFWWCM PFNCV ZXFN IFXMV ZFX JYFFM  WHNFX')