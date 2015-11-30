# -*- coding: utf-8 -*-

import subprocess
import sys
import os
from CeaserEncrypt.Alphabet import MyAlphabet

ENGLISH_ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
TURKISH_ALPHABET = ['a', 'b', 'c', 'ç' 'd', 'e', 'f', 'g', 'ğ' , 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş' , 't', 'u', 'ü', 'v', 'y', 'z']

#subprocess.Popen(r'explorer /select,"C:\Users\barin.huseyin\TEMP-WORKSPACE\CeaserEncryptionDemo\"')

# print "sys.argv[0] =", sys.argv[0]             1
# pathname = os.path.dirname(sys.argv[0])        2
# print 'path =', pathname
# print 'full path =', os.path.abspath(pathname)

letter=raw_input("Enter a letter or word")
    
print "Letter is:",letter
    
if letter not in ENGLISH_ALPHABET:
        
     print "not open hereeee"
    
    
print ENGLISH_ALPHABET.givePosOfLetter(letter)

