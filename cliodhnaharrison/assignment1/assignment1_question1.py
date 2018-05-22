#Using Python 3

import string

string_one = input()
string_two = input()

def anagram_finder(string_one, string_two, case_sensitive=False):
    anagram = True
    alphabet = list(string.printable)

    if case_sensitive:
        for char in alphabet:
            if anagram:
                if string_one.count(char) != string_two.count(char):
                    anagram = False
            else:
                return anagram
        return anagram

    else:
        #Case Insensitive so making sure only lowercase letters in strings
        string_one = string_one.lower()
        string_two = string_two.lower()
        for char in alphabet:
            if anagram:
                if string_one.count(char) != string_two.count(char):
                    anagram = False
            else:
                return anagram
        return anagram

print (anagram_finder(string_one, string_two))
