##Louis ONeal
##LOCBF@umkc.edu 
##CS 101L 
##Program 6 
##
##PROBLEM: Do Caesar Encryption/Decryption, including cracking a string w/ 
##  unknown Caesar key. 
##  
##Functions needed: 
##  Encrypt(string_text, int_key): Takes a string and integer key, returns 
##  the encryption of the string using that key. Note that for Caesar encryption, 
##  an encryption with key k (k in 1 - 25) is decrypted by doing the same process 
##  with key 26-k. Returns encrypted string using specified key. 
##  
##  Decrypt(string_text, int_key): Decrypts key by calling Encrypt with key 
##    26-int_key and returning the result. Done this way to make for a cleaner
##    breakdown of the problem. Returns decrypted string using specified key. 
##    
##  Crack(string_text): Decrypts a string by repeatedly calling Decrypt with each 
##    possible key (1 to 25) and remembering the one with a letter frequency 
##    closest to English based on counts of E, T, O, A, I, N. Returns tuple: 
##    decrypted string and decryption key. 
##    
##  Get_input(): Interacts with user, gets user choice of '1'-'4' and returns that 
##  value. If user enters anything else, prints brief error message and tries again. 
##  
##  Print_menu(): Prints menu. No user interaction. 
  
################################ 

import string

def Encrypt(string_text, int_key) -> str:
    EncryptedString = input('Enter (brief) text to encrypt:')
    for i in EncryptedString:
        print(chr)

    return

def Decrypt(string_text, int_key) -> str:
    return

def Crack(string_text):
    return 

def Get_input() -> str:
    my_num = input("1-4")
    return my_num

def main():
    ch = 'A'
    print(ord(ch))

    val = 65
    print(chr(val))

main()
