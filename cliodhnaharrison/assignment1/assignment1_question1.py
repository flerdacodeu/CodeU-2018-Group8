import string

string_one = input()
string_two = input()

alphabet = list(string.ascii_lowercase)

anagram = True

for char in alphabet:
    if anagram:
        if string_one.count(char) != string_two.count(char):
            anagram = False
    else:
        break

print (anagram)
