def find_valid_words(grid, word_dict, prefix_dict):
	seen_combinations = set()
	valid_words = set()
	shifts = ((1, 1), (0, 1), (1, 0), (-1, -1), (-1, 0), (0, -1), (1, -1), (-1, 1))
	for posx in range(len(grid)):
		for posy in range(len(grid[0])):
			visited_positions = set()
			curr_word = ""
			pos = (posx, posy)
			_search_words(grid, word_dict, prefix_dict, pos, shifts, 
						  curr_word, valid_words, seen_combinations, visited_positions)
	print valid_words

def _search_words(grid, word_dict, prefix_dict, pos, shifts, 
				  curr_word, valid_words, seen_combinations, visited_positions):
	if len(grid) > pos[0] >= 0 and len(grid[1]) > pos[1] >= 0:
		curr_word += grid[pos[0]][pos[1]]
		if is_prefix(curr_word, prefix_dict):
			if is_word(curr_word, word_dict):
				valid_words.add(curr_word)
			if ((pos, curr_word)) not in seen_combinations and pos not in visited_positions:
				for shift in shifts:
					_search_words(grid, word_dict, prefix_dict, (pos[0]+shift[0], pos[1]+shift[1]), 
								  shifts, curr_word, valid_words, seen_combinations, visited_positions)
		seen_combinations.add((pos, curr_word))
		visited_positions.add(pos)
	if pos in visited_positions:
		visited_positions.remove(pos)

def is_word(word, word_dict):
	if word in word_dict:
		return True
	return False

def is_prefix(prefix, prefix_dict):
	if prefix in prefix_dict:
		return True
	return False

def get_prefix_dict(word_dict):
	prefix_dict = set()
	for word in word_dict:
		for cidx in range(1, len(word)+1):
			prefix_dict.add(word[:cidx])
	return prefix_dict


word_dict = set(["car", "card", "cart", "cat"])
grid = [["a", "a", "r"], ["t", "c", "d"]]
prefix_dict = get_prefix_dict(word_dict)
find_valid_words(grid, word_dict, prefix_dict)

# assume all letters are lowercase
# word_dict is a set
# grid is a list of lists