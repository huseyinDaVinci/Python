# -*- coding: utf-8 -*-
import string
import os
from test.test_uu import plaintext
from random import choice
from _ast import Num
import sys
import subprocess
from CeaserEncrypt import Alphabet
from CeaserEncrypt.Alphabet import MyAlphabet
from telnetlib import STATUS



# Formatting the string in Python

ENGLISH_ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
TURKISH_ALPHABET = ['a', 'b', 'c', 'ç' 'd', 'e', 'f', 'g', 'ğ' , 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş' , 't', 'u', 'ü', 'v', 'y', 'z']



# initialize variables
D_status = {"E":"encrypt", "D":"decrypt"}
D_directoryNames = {"E":"EncryptedFiles", "D":"DecryptedFiles"}
D_alphabet = {"E":ENGLISH_ALPHABET, "T":TURKISH_ALPHABET}




turkishAlphabet = MyAlphabet(TURKISH_ALPHABET, 29)
englishhAlphabet = MyAlphabet(ENGLISH_ALPHABET, 26)

temp_list = []
cipherText = ""
plainText = ""
secret_word = "deron"
index = 0
orderCount = 7



def replaceWithEncrypt(letter):
    
    if(letter not in ENGLISH_ALPHABET):
        temp_list.append(letter)
        
    else:
        
        index = ENGLISH_ALPHABET.index(letter)
        if (index + orderCount >= 25):
                index = ((index + orderCount) % 25) - 1
        else:
                index = index + orderCount
            
        temp_list.append(ENGLISH_ALPHABET[index])
        
    
    
    
def replaceWithDecrypt(letter):
    
    if(letter not in ENGLISH_ALPHABET):
       
        temp_list.append(letter)
    else:
        
        index = ENGLISH_ALPHABET.index(letter)
        if (index - orderCount < 0):
                    
            index = (len(ENGLISH_ALPHABET)) + ((index - orderCount))
                   
        elif(index - orderCount == 0):
            index = 0
                                               
        else:
            index = index - orderCount
        
        temp_list.append(ENGLISH_ALPHABET[index])
    
def encryptWithCeaser(plainText):
    for letter in plainText:
        
        replaceWithEncrypt(letter)
    return temp_list

def decrypttWithCeaser(plainText):
    for letter in plainText:
        replaceWithDecrypt(letter)
    return temp_list


def encryptWithVigenere(plainText, key):
    
    counter = 0
    resVigenereText = []
    
    print "Before:Cipher of Encryption of Vigenere", resVigenereText
    
    if len(plainText) > len(key):
        isKeyLongerThanPText = 1
    else:
        isKeyLongerThanPText = 0

    for letter in plainText:
    
        if(letter not in ENGLISH_ALPHABET):
            resVigenereText.append(letter)  
        else:  
            if(counter >= len(key) and isKeyLongerThanPText):
                res = englishhAlphabet.giveNewPosOfLetter(letter, key[counter % len(key)], 1)
            else:
                res = englishhAlphabet.giveNewPosOfLetter(letter, key[counter], 1)
                
            resVigenereText.append(ENGLISH_ALPHABET[res])
        counter += 1
    
    
    print "ResVigeneree", string.join(resVigenereText, "")
    print "After:Cipher of Encryption of Vigenere", resVigenereText
    return resVigenereText
    
   
def decrypteWithVigenere(cipherText, key):
    counter = 0
    resVigenereText = []
    
    print "Before:Cipher of Decryption of Vigenere", resVigenereText
    if len(cipherText) > len(key):
        isKeyLongerThanPText = 1
    else:
        isKeyLongerThanPText = 0

    for letter in cipherText:
    
        if(letter not in ENGLISH_ALPHABET):
            resVigenereText.append(letter)  
        else:  
            if(counter >= len(key) and isKeyLongerThanPText):
                res = englishhAlphabet.giveNewPosOfLetter(letter, key[counter % len(key)], 0)
            else:
                res = englishhAlphabet.giveNewPosOfLetter(letter, key[counter], 0)
                
            resVigenereText.append(ENGLISH_ALPHABET[res])
        counter += 1
    print "After:Cipher of Decryption of Vigenere", resVigenereText
    return resVigenereText

def cleanList():
    cipherText = ""
    plainText = ""
    del temp_list[:]
    




def showValuesOfText():
    print "Plain text:", plainText
    print "Cypher text:", cipherText
    print "Temp List:", temp_list
    print "the length of Turkish alphabet:", len(TURKISH_ALPHABET)
    

def initialize():
    cleanList()
    directoryNames = [D_directoryNames["E"], D_directoryNames["D"]]
    createDirectories(directoryNames)
    

def checkAlphabetInput(alphabetName):
    
    while True:
        alphabetName = raw_input("Alphabet:Turkish or English (E,T):")
        
        if(alphabetName == "E" or alphabetName == "T"):
            alphabetName = D_alphabet[alphabetName]
            return 1
                    
        elif status == "exit" or status == "EXIT":
            sys.exit(0)          
        else:
            print "Please enter E or T for alphabet only!!"


    

def validateInput():

    global status, alphabetName
    
    alphabetName = []
    status = raw_input("Status: Encrypt or Decrypt (E,D) or exit to quit:")
    status = status.upper()
    
    if(status == "E" or status == "D"):    
        status = D_status[status]
        # if(checkAlphabetInput(alphabetName)):    
        return 1
           
    elif status == "exit" or status == "EXIT":
        sys.exit(0)
    else:
        print "Please enter E or D only!!"
        return 0


def writeEncrytedTextToFile(filename, cipherText):

    try:
        encryptedFile = open(D_directoryNames["E"] + "/" + filename, "wb")
        encryptedFile.write(cipherText)
        print "Encytpted file named ", filename , " saved successfully..."
    except:  # general catch here
        e = sys.exc_info()[0]
        raise e
    finally:
        encryptedFile.close()

def readEncytedFile(filenameEncrypted, filenameDecrypted):
    
    flag=1
    encryptedFileToOpen = None
    descrytedFile = None
    try:
        encryptedFileToOpen = open(D_directoryNames["E"] + "/" + filenameEncrypted, "r+")
        content = encryptedFileToOpen.read()
        print "content:", content
        descContent = decrypttWithCeaser(content)
        print "descContent:", descContent
        decryptedText = string.join(descContent, "")
        print "decryptedText:", decryptedText
        
        result = "decryptedText.txt"
        descrytedFile = open(D_directoryNames["D"] + "/" + filenameDecrypted, "wb")
        descrytedFile.write(decryptedText)
    
        print "Decrypted file named ", filenameDecrypted , " created successfully..."
    except IOError as e:
        print "IO Error:",e
        flag=0
    except Exception as e:
        print "Error:",e
        flag=0
    finally:
        if encryptedFileToOpen is not None:
            encryptedFileToOpen.close()
        if descrytedFile is not None:
            descrytedFile.close()
            
            
    return flag
 
def createDirectories(directories):
    
    for directoryName in directories:
        if not os.path.exists(directoryName):
            os.makedirs(directoryName)
        
def delDirectoires():
    try:
        if os.listdir(D_directoryNames["E"]) != []:
            print "Directory:/"+D_directoryNames["E"]+" content of this-->"
            
            print os.listdir(D_directoryNames["E"])
            os.system('rmdir /S "%s"' %D_directoryNames["E"])
            
        if os.listdir(D_directoryNames["D"]) != []:
            print "Directory:/"+D_directoryNames["D"]+" content of this-->"
            print os.listdir(D_directoryNames["D"])
            os.system('rmdir /S "%s"' %D_directoryNames["D"])
        
        #os.remove(D_directoryNames["E"])
        #os.remove(D_directoryNames["D"])
    except WindowsError as e:  #this is for exception handling in Python 
        print e
        
        
def list_files(path):
    # returns a list of names (with extension, without full path) of all files 
    # in folder path
    files = []
    for name in os.listdir(path):
        if os.path.isfile(os.path.join(path, name)):
            files.append(name)
    return files 

    
    
def decideFileOperations(cipherText, typeStatus):
    cleanList()
    if typeStatus == "E":
        while True:
            choice = raw_input("Do you want to save encrypted text as file(Y,N) to quit (exit):")  
            choice = choice.upper()
            if choice == "Y":
                filename = raw_input("Enter your file name:")
                writeEncrytedTextToFile(filename, cipherText)
                break
            elif choice == "N":
                break
            elif choice == "EXIT":
                print "Please enter a valid choice"
    else:  # this is for decryption file operations
        while True:
            
            # list the encrypted files 
                
            files = list_files(D_directoryNames["E"])
            for i in list_files(D_directoryNames["E"]):
                print i  
            if len(files) > 0:
                    
                filenameChosen = raw_input("Enter an encrypted file name:")            
                    
                filenameToDecryptFile = raw_input("Enter your decytpted file name:")
                    
                if(readEncytedFile(filenameChosen, filenameToDecryptFile)):
                    openExplorer()
            
            if len(files)==0:
                print "There no file under /",D_directoryNames["E"]
                
            break




def openExplorer():
    subprocess.Popen(r'explorer /select,"DecryptedFiles\"')

def __init__():     
    
    
    delDirectoires()
    
    while True: 
        
        initialize()
        if(validateInput()):     
            if(status == "encrypt"):
                plainText = raw_input("Enter your plainText:").strip().lower()  # strip will trim the string
                print "plain text you entered:", plainText
                encryptWithCeaser(plainText)
                cipherText = string.join(temp_list, "")
                secretKey = raw_input("Enter your key:")
                
                if cipherText is not None:
                    print "The cipher from cezar:", cipherText
                    cipherVigenere = encryptWithVigenere(cipherText, secretKey)
                    
                print "The cipher from vigenere:", cipherVigenere
                decideFileOperations(cipherText, "E")      
            else:
                choice = raw_input("Decrypte with file(1)or with cipher text(2) exit(0):").strip() 
                if choice == "2":
                    plainText = raw_input("Enter your cipherText:").strip().lower()  # strip will trim the string
                    
                    secretKey = raw_input("Enter your key:")
                    
                    if plainText is not None  and secretKey is not None:
                        plainVigenere = decrypteWithVigenere(plainText, secretKey)
                    
                    print "Plain of Vigenere", plainVigenere    
                    decrypttWithCeaser(plainVigenere)
                    cipherText = string.join(temp_list, "")
                    print string.join(temp_list, "")
                    
                elif choice == "1": 
                    decideFileOperations("", "D")
                                       
                elif choice == "0":
                    sys.exit(0)

__init__()


# function will be   K=(a,b)
# CHEKLIST
# büyük küçük harf kontrolü yapılacak  +++


# secret key ile bazı kelimelerin yerleri değişecek +++
# quick encryp/decrypt yaplacak
# selecting text file and ecrypt it then backup and send to ftp archive
#


    

