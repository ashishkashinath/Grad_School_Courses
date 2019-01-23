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
freq=[0]*26
for letter in text:
    freq[ord(letter)-ord('a')]+=1

mean=len(text)/26.0
print mean
sum=0
for i in freq:
    sum+=(float(i)/len(text)-1/26.0)**2

print sum/26
