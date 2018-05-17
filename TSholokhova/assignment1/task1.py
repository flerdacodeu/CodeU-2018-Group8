#only letters and spaces are not ignored
s1 = input()
s2 = input()
words1 = ''.join([c if c.isalpha() else ' ' for c in s1]).split()
words2 = ''.join([c if c.isalpha() else ' ' for c in s2]).split()
sort_letters = lambda words: sorted(list(map(lambda word: sorted(word.lower()), words)))
sort_letters_cs = lambda words: sorted(list(map(lambda word: sorted(word), words)))
if sort_letters_cs(words1) == sort_letters_cs(words2):
    print(s1, 'AND', s2, 'ARE CASE SENSITIVE ANAGRAMS')
elif sort_letters(words1) == sort_letters(words2):
    print(s1, 'AND', s2, 'ARE CASE INSENSITIVE ANAGRAMS')
else:
    print(s1, 'AND', s2, 'ARE NOT ANAGRAMS')