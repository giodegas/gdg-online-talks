#coding: utf-8

# oggi è una bella giornata

# today is a nice day

# Delia example: I'm going to meet my friend next to the bank (river bank or institution)

# Tokenization: to extract "words" from text

# lexem : specific text form of a word

# tokeziner function

# tre main aspect of function: identifier, list of parameters, result

# PyCharm from JetBrains

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

    tempString = inString
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

print('this is punctuation', punctuation)
myString = "I'm going to meet my friend next to the bank (river bank or institution)"

# First step of CL: Tokenization
lexemes = tokenize(myString)

# Second step: count occurrencies
lexCounts = countOccurrencies(lexemes)

print(lexCounts)
