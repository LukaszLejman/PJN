from nltk.tokenize import sent_tokenize
tmpHR = ''
tmpENG = ''
en = []
cr = []
open('EN.txt', 'w').close()
open('HR.txt', 'w').close()
for i in range(1,10):
    tmpENG = open('manuals/' + str(i) + '/english.txt', encoding='utf-8').read()
    tmpHR = open('manuals/' + str(i) + '/croatian.txt', encoding='utf-8').read()
    with open("EN.txt", "a", encoding='utf-8') as myfile:
        myfile.write(tmpENG)
    with open("HR.txt", "a", encoding='utf-8') as myfile:
        myfile.write(tmpHR)
    print(i)
