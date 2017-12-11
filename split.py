import re
result = open('korpus.txt', 'r', encoding='utf-8').readlines()
open('angResult.txt', 'w', encoding='utf-8')
open('hrResult.txt', 'w', encoding='utf-8')
angResult = open('angResult.txt', 'a', encoding='utf-8')
hrResult = open('hrResult.txt', 'a', encoding='utf-8')
for line in result:
    a,b,c = re.split(r'\t', line);

    angResult.write(a+'\n')
    hrResult.write(b+'\n')
