# as soon as the program runs it asks the user to input a file path which is saved in a variable called filepath to later be tokenized
import sys
filepath = sys.argv[-1]

# PartA.1
# Write a method/function that reads in a text file and returns a list of the tokens in that file. 
# For the purposes of this project, a token is a sequence of alphanumeric characters, 
# independent of capitalization (so Apple, apple, aPpLe are the same token). 
# You are not allowed to use regular expressions, and you are not allowed to import a tokenizer (e.g. from NLTK), 
# since you are being asked to write a tokenizer.
# returns List<Token>
def tokenize(filepath):
    tokens = []
    with open(filepath, 'r') as file:
        current_token = ''
        # read each character in the file and convert to lowercase
        for char in file.read():
            if char.isalnum():
                current_token += char.lower()
            else:
                if current_token:
                    tokens.append(current_token)
                    current_token = ''
        
        # confirm there's nothin left in the file
        if current_token:
            tokens.append(current_token)
    return tokens

# PartA.2
# Write another method/function that counts the number of occurrences of each token in the token list. 
# Remember that you should write this assignment yourself from scratch so you are not allowed to import a counter 
# when the assignment asks you to write that method.
# returns Map<Token, Count>
def computeWordFrequencies(token_array):
    frequency_map = {}
    for token in token_array:
        if token in frequency_map:
            frequency_map[token] += 1
        else:
            frequency_map[token] = 1
    return frequency_map

# PartA.3
# Finally, write a method that prints out the word frequency count onto the screen. 
# The print out should be ordered by decreasing frequency (so, the highest frequency words first).
# does not return anything
def get_count(pair):
    return pair[1]

def print_frequencies(frequency_map):
    sorted_frequencies = sorted(frequency_map.items(), key=get_count, reverse=True)
    for token, count in sorted_frequencies:
        print(f"{token} = {count}")

tokens = tokenize(filepath)
frequencies = computeWordFrequencies(tokens)
print_frequencies(frequencies)