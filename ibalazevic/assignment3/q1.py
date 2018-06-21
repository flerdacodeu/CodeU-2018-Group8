from collections import defaultdict
import unittest

def find_valid_words(grid, prefix_dict):
    """
    A method that finds all the valid words from a 
    dictionary in a grid of letters. The assumption
    is that all the letters in the grid are lowercase.
        - grid - list of lists, a 2D grid of characters
        - prefix_dict - dict, tree-like dictionary in 
                        which the keys are the prefixes
                        and values the following letters
                        for each of the prefix in its
                        corresponding valid word
        Returns: a set of all the valid words found in 
                 the grid.

    """
    valid_words = set()
    shifts = ((1, 1), (0, 1), (1, 0), (-1, -1), 
              (-1, 0), (0, -1), (1, -1), (-1, 1))
    for posx in range(len(grid)):
        for posy in range(len(grid[0])):
            visited_positions = set()
            word_list = []
            curr_word = ""
            pos = (posx, posy)
            _search_words(grid, prefix_dict, pos, shifts, curr_word, 
                          valid_words, visited_positions, word_list)
    return valid_words

def _search_words(grid, prefix_dict, pos, shifts, curr_word, 
                  valid_words, visited_positions, word_list):
    """
    A recursive helper method to find all the valid words 
    from a dictionary in a grid of letters. 
        - grid - list of lists, a 2D grid of characters
        - prefix_dict - dict, tree-like dictionary in 
                        which the keys are the prefixes
                        and values the following letters
                        for each of the prefix in its
                        corresponding valid word
        - pos - tuple of ints, current position in the grid
        - shifts - list of tuples, the 8 possible moves moves
                   from the current position
        - curr_word - str, current string of letters that has
                      been formed by moving through the grid
        - valid_words - list, the list of valid words that have
                        been found in the grid so far
        - visited_positions - set of tuples, keeps track of all
                              the positions we"ve visited so far
                              so we don"t end up in the same twice
        - word_list - list, keeps track of all the prefixes in the
                      current recursive call for a given word. 
    """
    if len(grid) > pos[0] >= 0 and len(grid[0]) > pos[1] >= 0:
        curr_word += grid[pos[0]][pos[1]]
        if is_prefix(curr_word, prefix_dict):
            word_list.append(curr_word)
            if pos not in visited_positions:
                if is_word(curr_word, prefix_dict):
                    valid_words.add(curr_word)
                visited_positions.add(pos) 
                for shift in shifts:
                    _search_words(grid, prefix_dict, (pos[0]+shift[0], pos[1]+shift[1]), 
                                  shifts, curr_word, valid_words, visited_positions, word_list)
                visited_positions.remove(pos)
            if not prefix_dict[curr_word] or prefix_dict[curr_word] == set(["END"]):
                del prefix_dict[curr_word]
                prefix_dict[curr_word[:-1]].remove(curr_word[-1])
            word_list.pop()
    
        
    
def is_word(word, prefix_dict):
    """
    A method that checks whether a given string
    is present in the dictionary of words.
        - word - str, current string of letters
        - prefix_dict - dict, tree-like dictionary in 
                        which the keys are the prefixes
                        and values the following letters
                        for each of the prefix in its
                        corresponding valid word
        Returns: True if a word is valid, False otherwise.
    """
    return word in prefix_dict and "END" in prefix_dict[word]

def is_prefix(prefix, prefix_dict):
    """
    A method that checks whether a given string
    is a valid prefix for any of the words.
        - prefix - str, current string of letters
        - prefix_dict - dict, tree-like dictionary in 
                        which the keys are the prefixes
                        and values the following letters
                        for each of the prefix in its
                        corresponding valid word
        Returns: True if a prefix is valid, False otherwise.
    """
    return prefix in prefix_dict

def get_prefix_tree(word_dict):
    """
    A method that creates the prefix tree for all the 
    words in the word_dict.
        - word_dict - set, contains all the valid words
        Returns: dict, tree-like dictionary in 
                 which the keys are the prefixes
                 and values the following letters
                 for each of the prefix in its
                 corresponding valid word
    """
    prefix_dict = defaultdict(set)
    for word in word_dict:
        for cidx in range(len(word)):
            prefix_dict[word[:cidx]].add(word[cidx])
        prefix_dict[word].add("END")
    return prefix_dict

class WordSearchTest(unittest.TestCase):
    
    def test_base(self):
        word_dict = set(["car", "card", "cart", "cat", "cat"])
        grid = [["a", "a", "r"], ["t", "c", "d"]]
        prefix_dict = get_prefix_tree(word_dict)
        self.assertEqual(find_valid_words(grid, prefix_dict), 
                                set(["car", "card", "cat"]))

  
    def test_empty(self):
        word_dict = set([])
        grid = [[]]
        prefix_dict = get_prefix_tree(word_dict)
        self.assertEqual(find_valid_words(grid, prefix_dict), set([]))

    def test_1D(self):
        word_dict = set(["c", "af", "bc", "b"])
        grid = [["c", "b", "b", "b", "b", "b", "b", "b", "b", "b", "a", "f"]]
        prefix_dict = get_prefix_tree(word_dict)
        self.assertEqual(find_valid_words(grid, prefix_dict), 
                                set(["c", "bc", "b", "af"]))


    def test_same_cell_twice(self):
        word_dict = set(["car", "card", "cart", "cat", "catc"])
        grid = [["a", "a", "r"], ["t", "c", "d"]]
        prefix_dict = get_prefix_tree(word_dict)
        self.assertEqual(find_valid_words(grid, prefix_dict), 
                                set(["car", "card", "cat"]))


if __name__ == "__main__":
    unittest.main()
