__author__ = 'Sunny'
text='ethicslawanduniversitypoliciestodefendasystemyouneedtobeabletothinklik' \
    'eanattackerandthatincludesunderstandingtechniquesthatcanbeusedtocompro' \
    'misesecurityhoweverusingthosetechniquesintherealworldmayviolatethelawo' \
    'rtheuniversitysrulesanditmaybeunethicalundersomecircumstancesevenprobi' \
    'ngforweaknessesmayresultinseverepenaltiesuptoandincludingexpulsioncivi' \
    'lfinesandjailtimeourpolicyineecsisthatyoumustrespecttheprivacyandprope' \
    'rtyrightsofothersatalltimesorelseyouwillfailthecourseactinglawfullyand' \
    'ethicallyisyourresponsibilitycarefullyreadthecomputerfraudandabuseactc' \
    'faaafederalstatutethatbroadlycriminalizescomputerintrusionthisisoneofs' \
    'everallawsthatgovernhackingunderstandwhatthelawprohibitsyoudontwanttoe' \
    'nduplikethisguyifindoubtwecanreferyoutoanattorneypleasereviewitsspolic' \
    'iesonresponsibleuseoftechnologyresourcesandcaenspolicydocumentsforguid' \
    'elinesconcerningproperuseofinformationtechnologyatumaswellastheenginee' \
    'ringhonorcodeasmembersoftheuniversitycommunityyouarerequiredtoabidebyt'

cipher_text=''
key_cipher='uvwxyz'
key='uvwxyz'
for i in range(0,len(text)):
    cipher_text+=chr((ord(key_cipher[i%len(key_cipher)])+ord(text[i])-2*ord('a'))%26+ord('a'))
#print cipher_text

sum=0
freq_freq=[[0]*26 for i in range(len(key))]
k=0
for letter in cipher_text:
    freq_freq[k%len(key)][ord(letter)-ord('a')]+=1
    k+=1

for i in freq_freq:
    for k in i:
        sum+=(float(k)/len(text)*len(key)-1/26.0)**2

print sum/26/len(key)