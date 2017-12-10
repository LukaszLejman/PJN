from nltk.tokenize import sent_tokenize
import os
numberOfManuals = 46
tmpHR = ''
tmpENG = ''
open('korpus.txt', 'w').close()

for i in range(1, numberOfManuals+1):
    englishVersion = ''
    croatianVersion = ''
    tmpEN = open('manuals/' + str(i) + '/english.txt', encoding='utf-8').readlines()
    tmpHR = open('manuals/' + str(i) + '/croatian.txt', encoding='utf-8').readlines()
    open('EN.txt', 'w').close()
    open('HR.txt', 'w').close()
    for line in tmpEN:
        if line not in ['\n', '\r\n']:
            line = line.replace('...', '')
            line = line.replace('..', '')
            line = line.replace('•', '')
            line = line.replace('', '')
            line = line.replace('', '')
            line = line.replace('@@', '')
            line = line.replace('@@@', '')
            englishVersion = englishVersion + line
    for line in tmpHR:
        if line not in ['\n', '\r\n']:
            line = line.replace('...', '')
            line = line.replace('..', '')
            line = line.replace('•', '')
            line = line.replace('', '')
            line = line.replace('', '')
            line = line.replace('@@', '')
            line = line.replace('@@@', '')
            croatianVersion = croatianVersion + line
    tokenizeEN = sent_tokenize(englishVersion)
    tokenizeHR = sent_tokenize(croatianVersion)
    EN = open('EN.txt', 'w', encoding='utf-8')
    HR = open('HR.txt', 'w', encoding='utf-8')
    for j in tokenizeEN:
        if not str(j) in ['\n', '\r\n']:
            EN.write("%s\n" % j)
    for j in tokenizeHR:
        if not str(j) in ['\n', '\r\n']:
            HR.write("%s\n" % j)
    EN.close()
    HR.close()
    os.system('cd > tmp' + str(i) + '.dict')
    os.system('hunalign\hunalign.exe -text -utf -realign tmp' + str(i) + '.dict EN.txt HR.txt > aligned' + str(i) + '.txt')
    os.system('del tmp' + str(i) + '.dict')
    with open('korpus.txt', 'a', encoding='utf-8') as resultFile:
        with open('aligned' + str(i) + '.txt', 'r', encoding='utf-8') as partAlign:
            for line in partAlign:
                resultFile.write(line)
        os.system('del ' + 'aligned' + str(i) + '.txt')

    print(i)
