'''
Created on Apr 7, 2015

@author: barin.huseyin
'''

class MyAlphabet:
    
    
    alphabetLetters=[]
    letterCount=0
    count=0
    
    def __init__(self,alphabetLetters,letterCount):
        self.alphabetLetters=alphabetLetters
        self.letterCount=letterCount
        MyAlphabet.count+=1
        
    
    def giveInfo(self):
        
        print "The alphabet letters:",self.alphabetLetters,"\nLetter count in the alphabet:",self.letterCount,"\nThe Alphabet created so far:",MyAlphabet.count
        
    
    
    def givePosOfLetter(self,letter):
        return self.alphabetLetters.index(letter)    

    def giveNewPosOfLetter(self,letterToMove,keyLetter,type):#a   #b
        indexKey=self.alphabetLetters.index(keyLetter)  
        indexLetterMove=self.alphabetLetters.index(letterToMove)
        
        if indexKey is 0:
            return indexLetterMove
        else:
            if type is 1:
                if indexKey+indexLetterMove>=25:
                    return (indexKey+indexLetterMove)%25-1
                else:
                    return indexKey+indexLetterMove
            else:
                if  indexKey==0:
                    return indexLetterMove
                elif indexLetterMove-indexKey <0:
                    return len(self.alphabetLetters)-(indexLetterMove-indexKey)*-1
                else:
                    return indexLetterMove-indexKey
        
        
        
        
            