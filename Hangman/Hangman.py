# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 10:20:20 2021
@author: Ainish
"""

import random

def getWordRepository():
    """Function that reads words from a repository and returns a list 
    of words"""
    
    Repository =  ['Jazz', 'Rock', 'Popular', 'Blues', 'Country']    
    return Repository

def getWordRepository2():
    File    = open('HangmanWords.txt','r')
    Words   = File.readlines()
    return Words
    
def RandomWord():
    #Repository = getWordRepository()
    Repository = getWordRepository2()
    return Repository[(random.randint(0, len(Repository)-1))].lower()

def AllowedCharacters():
    return set('abcdefghijklmnopqrstuvwxyz')

def CharactersAvailable(LettersGuessed):
    C = list(AllowedCharacters() - set(LettersGuessed))
    C.sort()
    return( " ".join(C))
    
def WordGuessed(GameWord, LettersGuessed):
    for letter in GameWord:
        if letter not in LettersGuessed:
            return False
    return True

def ShowProgress(GameWord, LettersGuessed):
    string = ''
    for letter in GameWord:
        if letter in LettersGuessed:
            string = string + letter
        else:
            string = string + '-'
    print("\n",string)
    return

def Hangman():
    GameWord        = RandomWord().lower()
    guesses         = 8    
    LettersGuessed  = []
    Stupiditycount  = 0
    
    print("\n\nLet's play! Your word has",len(GameWord), 'letters\n')
    
    while guesses >=1:
        print('\n You have', guesses, 'guesses left. Guess from the below letters \n', CharactersAvailable(LettersGuessed))
        l = input('Guess a letter ').lower()
        
        if l in LettersGuessed:
            print(l, ' has already been guessed')
            Stupiditycount +=1 
            
            if Stupiditycount > 8:
                print('You have repeated too many letters, you lost!')
                return
            continue
        
        else:
            LettersGuessed.append(l)
            if l in GameWord:
                print('Good Guess!')
                if WordGuessed(GameWord, LettersGuessed):
                    print('Congrtulations, you Won!')
                    return
            else:
                print('Letter not in word, you lost a guess')
                guesses +=-1
            
            ShowProgress(GameWord, LettersGuessed)        
    print('You ran out of guesses. The word was', GameWord)
    return 

Hangman()



