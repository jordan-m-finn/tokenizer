# Tokenizer

A Python-based text analysis tool that processes text files and analyzes token frequencies.

## Features

### Part A: Token Frequency Analysis
- Tokenizes text files into individual words
- Counts frequency of each token
- Displays tokens sorted by frequency in descending order
- Case-insensitive processing (e.g., "Hello" and "hello" are treated as the same token)
- Handles ASCII alphanumeric characters
- Non-ASCII characters are skipped during processing

### Part B: Common Token Analysis
- Compares two text files
- Identifies common tokens between files
- Returns the count of shared tokens

## Usage

### Token Frequency Analysis
```bash
python PartA.py path/to/file.txt >output.txt
```