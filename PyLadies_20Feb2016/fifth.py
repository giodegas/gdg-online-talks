#coding: utf-8

from string import punctuation
from collections import Counter

MY_PUNCTUATION = punctuation

dVocabulary = Counter()

def tokenize(inString):
    global separatorsList
    '''
    :param inString:
    :return: list of tokens (or lexems)
    '''
    out = []
    sP = set(separatorsList)
    sP.remove('@')
    sP.add('\n')

    tempString = inString.lower() # normalize version of the text

    for s in sP:
        tempString = tempString.replace(s, ' ')

    tempOut = tempString.split(' ')

    for lex in tempOut:
        if len(lex)>0:
            out.append(lex)
    return out

def countOccurrencies(lexemList):
    '''

    :param lexemList: iput sentence list of lexemes
    :return: a dictionary of lexems and their counts
    '''
    out = Counter()
    out.update(lexemList)
    return out

# MAIN ----

separatorsList = list(MY_PUNCTUATION)

text = open('mytext.txt','r').read()

# First step of CL: Tokenization
lexemes = tokenize(text)

# Second step: count occurrencies
dVocabulary = countOccurrencies(lexemes)

for lex in dVocabulary:
    print(lex, dVocabulary[lex])

print('all lexemes:')
print(dVocabulary.keys())
print(dVocabulary.values())