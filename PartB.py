import sys
import importlib.util

# import PartA without running its main code
spec = importlib.util.spec_from_file_location("PartA", "./PartA.py")
PartA = importlib.util.module_from_spec(spec)
spec.loader.exec_module(PartA)

if len(sys.argv) < 3:
    print("Error: Please provide exactly two file paths")
    sys.exit(1)

filepath_one = sys.argv[1]
filepath_two = sys.argv[2]

# PartB
# O(n) "linear" runtime because each function/method within operates separately in linear time
def compare_tokens(filepath_one, filepath_two):
    try:
        tokens_one = PartA.tokenize(filepath_one)
        tokens_two = PartA.tokenize(filepath_two)
        
        if not tokens_one or not tokens_two:
            print("Error: One or both files are empty")
            sys.exit(1)

        # set() method converts the total number of tokens m of each tokenized file so O(m) "linear"
        # .intersection() method compares the two sets of tokens so O(m) "linear" but uses the smaller set
        common_tokens = set(tokens_one).intersection(set(tokens_two))
        return len(common_tokens)
    except Exception as e:
        print(f"Error comparing files: {str(e)}")
        sys.exit(1)

print(compare_tokens(filepath_one, filepath_two))
