from collections import defaultdict
def words_anagrams(word1, word2, case_sensitive):
    """Checks if two words are anagrams.

    :param word1: first word of the two
    :param word2: second word of the two
    :param case_sensitive: boolean variable to determine the case sensitivity
    :return: True if they are anagrams, False if they are not
    """
    if len(word1) != len(word2):
        return False

    if case_sensitive == False:
        word1 = word1.lower()
        word2 = word2.lower()

    letters=defaultdict(lambda: 0)

    for letter in word1:
        letters[letter] += 1

    for letter in word2:
        if letters[letter]==0:
            return False
        letters[letter] -= 1

    for letter in letters:
        if letters[letter] != 0:
            return False

    return True

def sent_anagrams(sent1, sent2, case_sensitive):
    """Checks if two sentences are anagrams (Works with punctuation only if the punctuation symbol is separated from
    the words or is right after the same word in both sentences)

    :param sent1: first sentence of the two
    :param sent2: second setence of the two
    :param case_sensitive: boolean variable to determine the case sensitivity
    :return: True if they are anagrams, False if they are not
    """
    sent1 = sent1.split()
    sent2 = sent2.split()

    used = []            #List where I store the words I`ve matched

    if len(sent1) != len(sent2): return False

    for word in sent1:
        for word2 in sent2:
            if word2 not in used and words_anagrams(word,word2,case_sensitive) == True:
                used.append(word2)

    if len(used) == len(sent2):
        return True
    return False
