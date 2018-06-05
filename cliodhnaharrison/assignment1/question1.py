#Using Python 3

import string

#Input through command line
string_one = input()
string_two = input()

def anagram_finder(string_one, string_two, case_sensitive=False):
    anagram = True

    if len(string_one) != len(string_two):
        return False

    #Gets a list of ascii characters
    alphabet = list(string.printable)

    if not case_sensitive:
        #Case Insensitive so making sure only lowercase letters in strings
        string_one = string_one.lower()
        string_two = string_two.lower()

    for char in alphabet:
        if anagram:
            #Counts occurences of a character in both strings
            #If there is a difference it returns False
            if string_one.count(char) != string_two.count(char):
                anagram = False
        else:
            return anagram
    return anagram



#My Testing
#print (anagram_finder(string_one, string_two))
