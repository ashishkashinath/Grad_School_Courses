__author__ = 'Sunny'
import operator
def check_dist(values):
    std_dist=[8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.996,0.153,.772,4.025,2.406,6.749,7.507,1.929,.095,5.987,6.327,9.056,2.758,0.978,2.360,.150,1.974,0.074]
    dist_list=[]
    for i in range(0,26):
        sum=0
        print "Offset: ",i
        for j in range(0,26):
            sum+=(values[j]-std_dist[(i+j)%26])**2
        print "Distance: ",sum
        dist_list.append(sum)
    return dist_list.index(min(dist_list))

def check_key(cipher,key):
    output=''
    for i in range(0,len(cipher)):
        output+=chr((ord(cipher[i])+ord(key[i%len(key)])-ord('A')*2)%26+ord('A'))
    return output
cipher='ULPKXWRJUGCCQDLBVKVINLCTZEVOKNLYCWQLYTCRQBMYJASZDWWLMIKZEGLIMKLLCFIMVEZYGMIAPFWVJJBSALUKEZEAYJXETWWXRYZMCKU' \
       'IDIAXGLVBIVPJUCGCQEAMRWSCEUIENXZFUNZIKIYVUEVPGKAHXKVWEGWFGWBSSNFQIZNGGVOLMTFZCPIVNWIWVHDPJMRMMMDSHURLQNZUIZVMWSNVYXW' \
       'GSLZJYALKJVXXATFCEASZXSNZJRAPUOIDXGDMWYVWLLLUTJRNTVYEOMIWANPYEBLAHKZKZTLSRPXPPFNZXEBTGHRIHVZFLVKYLTSNZJRUZVYIIGZJHNFB' \
       'VIAZSZIXMCKYTOWBSWXZNGQADCEZWWQEUKCIULLCTNGWXHOKZVANAYEXIIYVYCZGBCAWRGIVRAHVZVQYYGFYIZYULPKXWRJUGCCQDZYRQMTJTUJZHWYEU' \
       'KCIULLCTVPBSWIITEVOUIDKYBPJMTDIVNWJIVGBTUYTMCXEGAIVTPTUUCBSZTLBDNEZPVYJDKVPVUIJYVOUIDKYBLLCFIETSSLUIIADSMJPQXEAIENQIV' \
       'AHXNYKSSFXJVQEZGJCEZOLISMIIVAHGMEKEAWVWCIYQUUQIZDSLPDXQDLBVJVMEAWRGPGAGMJDFTPLISMIIVKOTCEAJKNVHFCEANZNMVQWUJDFTPLIUJWW' \
       'MQUETOVZOHGMEKEAWRGQMLFMTMCXEGFFBCZPDUKZHBPUBEJPWRQBRNVITKYUVRCXTYIJJTPYUCDWAFWMKCIMWWWKMSVTUZIJRBTWLWJYVOSNZJRELKCEQS' \
       'TGWXZIEKLKYZIXPPMHZOILDLUKZWESAWYLYMDLCFIILHZYKCIZCWKLDVQYYMLNTMNLYUXVQXAHRGWBZHLFQMLPLBVDVLPULPKXQZFEVTWBZDUNZRNZJWVH' \
       'IVEAMLIGWYKNZOYBTGHRGXPPWZWVVOFWXKCEBEZCJDWIGAICVXQZFIWOLMCAAYOSNYGNSZMVRXIIXILEGCEXVQXAHROIWYWMVGJIDYCMZRQYLBVAMNEZUDZRLX'


pair_dic=[]
#for i in range(0,len(cipher)-3):
#    cur=cipher[i:i+3]
#    if cur in pair_dic:
#        pair_dic[cur]+=1
#    else:
#        pair_dic[cur]=1
for i in range(0,26):
    pair_dic.append(0)



possible_word=''
for j in range(0,7):
    for i in range(0,26):
        pair_dic[i]=0
    for i in range(0,150):
        pair_dic[(ord(cipher[(i*7+j)])-ord('A'))%26]+=1.0/150
    possible_word+=chr(check_dist(pair_dic)+ord('A'))
print possible_word
print check_key(cipher,possible_word)
actual_key=''
for letter in possible_word:
    actual_key+=chr((-1*(ord(letter)-ord('A')))%26+ord('A'))
print actual_key
#output=''
#for i in cipher:
#    output+=chr((ord(i)-ord('A')+22)%26+ord('A'))
#print output
#most_freq=max(pair_dic.iteritems(),key=operator.itemgetter(1))[0]
#for i in range(0,len(cipher)-3):
#    if cipher[i:i+3]==most_freq:
#        print i