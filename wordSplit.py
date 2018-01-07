def wordSplit(string):
    myDict = {'this':1,'is':2,'a':3,'sentence':4,'but':5,'how':6,'would':7,'you':8,'know':9,'it':10}
    wordFragment = ''
    finalSentence = ''

    for c in string:
        wordFragment += c
        if wordFragment in myDict:
            finalSentence += wordFragment + ' '
            wordFragment = ''

    return finalSentence.strip()
