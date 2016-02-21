#coding: utf-8

from string import punctuation

MY_PUNCTUATION = punctuation

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
    :return: a list of tuples with lexemes appearing only once and their respective count
    '''
    out = []
    lexemSet = set(lexemList)
    for lex in lexemSet:
        out.append((lex, lexemList.count(lex)))
    return out

# MAIN ----

separatorsList = list(MY_PUNCTUATION)

text = open('mytext.txt','r').read()

# First step of CL: Tokenization
lexemes = tokenize(text)

# Second step: count occurrencies
lexCounts = countOccurrencies(lexemes)

for tup in lexCounts:
    print(tup)
