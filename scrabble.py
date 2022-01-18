# ASSIGNMENT #1, by Logan Kulesus, Allen Schneider, and Diego Santander
import time


# Function for testing runtime of any given function
def test_runtime(f, arg):
    a = time.time()
    f(arg)
    b = time.time()
    print("\nRuntime of given function in seconds:\n", b - a)


# Function that returns the calculation for the sum of incremental integers
def sum_integers(x):
    return (x * (x + 1)) / 2


# Function that uses a recursive binary search to find a specific word in a word list
def bin_search(search_word, all_words, first_index, last_index):
    if last_index - first_index >= 0:
        mid_index = (last_index + first_index) // 2
        if search_word < all_words[mid_index]:
            return bin_search(search_word, all_words, first_index, mid_index - 1)
        elif search_word > all_words[mid_index]:
            return bin_search(search_word, all_words, mid_index + 1, last_index)
        elif search_word == all_words[mid_index]:
            return True
    else:
        print("not found")
        return False


# Function that searches a word list for a given word to verify that it can be made from a given tile set
def word_in_tiles(search_word, tiles):
    counter = 0
    word_char_list = list(search_word)
    for letter in word_char_list:
        if letter in tiles:
            counter += 1
    if counter == len(search_word):
        return "The word '" + search_word + "' can be made with the given tiles."
    else:
        return "The word '" + search_word + "' can NOT be made with the given tiles."


# Function that finds and returns all possible words formed from a given tile set
def words_from_tiles(tiles, all_words):
    found_words = ""
    tile_letters_list = list(tiles)
    tile_letters_list.sort()
    for word in all_words:
        if len(word) == len(tiles):
            compare_list = list(word)
            compare_list.sort()
            if tile_letters_list == compare_list:
                found_words += (word + " ")
    return found_words


# Function that takes a spelling bee puzzle string with the "middle letter" at the beginning of the string,
# and calculates/returns all possible words in the puzzle using the first letter.
def words_in_spelling_bee_puzzle(puzzle_string, all_words):
    possible_word_list = ""
    spelling_bee_letters = list(puzzle_string)
    for word in all_words:
        compare_list = list(word)
        if len(compare_list) <= len(spelling_bee_letters) and spelling_bee_letters[0] in compare_list and all(
                letter in spelling_bee_letters for letter in compare_list):
            counter = 0
            temp_letters = list(puzzle_string)
            for i in range(len(compare_list)):
                if compare_list[i] in temp_letters:
                    temp_letters.remove(compare_list[i])
                else:
                    counter += 1
            if counter == 0:
                possible_word_list += (word + " ")
    return possible_word_list


def find_best_bingo_tiles(all_words):
    tiles = []
    largest_tile_set = []
    largest_matches = 0

    # Create list of sorted letters that are 8 letters long to be used as tiles
    for word in all_words:
        if len(word) == 8:
            a = list(word)
            a.sort()
            tiles.append(a)
    # Sort the created list in order to sequentially check tiles
    tiles.sort()

    # Begin keeping track of how many tile sets are the same, and if the current set of
    # tiles has the largest matches, then save that tile and its matches as the new
    # largest tile set. Return the tile set after all tiles in list are checked.
    counter = 0
    previous = tiles[0]
    for tile_set in tiles:
        if tile_set == previous:
            counter += 1
        else:
            if counter > largest_matches:
                largest_tile_set = previous
                largest_matches = counter
            counter = 1
        previous = tile_set
    return [largest_tile_set, largest_matches]


# Main method to be ran when scrabble.py is ran
if __name__ == '__main__':

    # Increase recursion limit just to be safe
    import sys
    sys.setrecursionlimit(1500)

    # Open words.txt and save the entire dictionary to a list
    word_file = open('words.txt', 'r')
    word_list = word_file.read().split()
    word_file.close()

    # 1
    print("\n1.) Printing out the sum of the first 9 positive integers... ")
    print(int(sum_integers(9)))

    # 2
    print("\n2.) Checking to see if the word 'cat' is valid... ")
    word_found = bin_search("cat", word_list, 0, len(word_list))
    if word_found:
        print("The word 'cat' was found to be a valid word.")
    else:
        print("The word 'cat' is not a valid word.")

    # 3
    print("\n3.) Checking if the words 'hey' and 'man' can be made from the set of tiles: [a, y, b, e, t, n, h, q, w]")
    tile_list = list("aybetnhqw")
    print(word_in_tiles("hey", tile_list))
    print(word_in_tiles("man", tile_list))

    # 4
    print("\n4.) Printing all words found using set of tiles 'retains':")
    tile_words = words_from_tiles('retains', word_list)
    print(tile_words)

    # 5
    print("\n5.) All common words that are in the Figure 1: A Spelling Bee Puzzle.")
    print("The puzzle has the middle letter 'L,' with the rest of the letters being 'A,' 'B,' 'C,' 'I,' 'N,' 'R.':")
    possible_words = words_in_spelling_bee_puzzle('labcinr', word_list)
    print(possible_words)

    # 6
    print("\n6.) Determine 8-letter tile set that matches the most words in the dictionary:")
    bingo_vals = find_best_bingo_tiles(word_list)
    print("The tile set with most matches was " + str(bingo_vals[0]) + " with " + str(bingo_vals[1]) + " matches.")

    # Runtime Testing
    test_runtime(find_best_bingo_tiles, word_list)