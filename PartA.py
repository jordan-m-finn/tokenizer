# as soon as the program runs it asks the user to input a file path which is saved in a variable called filepath to later be tokenized
import sys

# PartA.1
# O(n) "linear" where n is the file length beacause each character is read once and 
# .lower(), .isascii(), and .isalnum() both operate in O(1) "constant" time
def tokenize(filepath):
    try:
        tokens = []
        with open(filepath, 'r', encoding='utf-8') as file:
            current_token = ''
            for char in file.read():
                # Simply skip non-ASCII characters but keep processing
                if char.isascii() and char.isalnum():
                    current_token += char.lower()
                else:
                    if current_token:
                        tokens.append(current_token)
                        current_token = ''
            
            if current_token:
                tokens.append(current_token)
        return tokens
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        sys.exit(1)

# PartA.2
# O(m) "linear" where the function iterates through each m token once 
def computeWordFrequencies(token_array):
    frequency_map = {}
    for token in token_array:
        if token in frequency_map:
            frequency_map[token] += 1
        else:
            frequency_map[token] = 1
    return frequency_map

# PartA.3
def get_count(pair):
    return pair[1]

# This is O(n log n) "linearithmic"
# the sorted() method is O(n log n) "linearithmic" because it uses a sorting algorithm 
# that has a worst-case runtime of O(n log n) where n is the number of elements in the list
# .items() runs in O(k) "linear" where k is the number of key-value pairs in the dictionary
def print_frequencies(frequency_map):
    sorted_frequencies = sorted(frequency_map.items(), key=get_count, reverse=True)
    for token, count in sorted_frequencies:
        print(f"{token} = {count}")

# Check if command line argument is provided
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Please provide a file path as command line argument")
        sys.exit(1)
    
    filepath = sys.argv[1]
    tokens = tokenize(filepath)
    frequencies = computeWordFrequencies(tokens)
    print_frequencies(frequencies)

# If you are confused on how to run this type in the terminal:
# python PartA.py <file path> >output.txt