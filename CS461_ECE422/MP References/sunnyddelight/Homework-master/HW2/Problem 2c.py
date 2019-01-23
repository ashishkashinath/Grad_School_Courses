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
key='uvwxyz'
for i in range(0,len(text)):
    cipher_text+=chr((ord(key[i%len(key)])+ord(text[i])-2*ord('a'))%26+ord('a'))
#print cipher_text
for i in range(0,len(key)):
    freq=[0]*26
for letter in cipher_text:
    freq[ord(letter)-ord('a')]+=1

mean=len(cipher_text)/26.0
sum=0
for i in freq:
    sum+=(float(i)/len(text)-1/26.0)**2

print sum/26
