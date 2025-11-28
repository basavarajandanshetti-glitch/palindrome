#!/usr/bin/env python3
import sys

# Default argument
default_string = "madam"

# If arguments are provided, use them
if len(sys.argv) >= 2:
    s = " ".join(sys.argv[1:])
    print("Using user-provided input.")
else:
    # No arguments → use default string
    s = default_string
    print(f"No arguments provided. Using default value: '{default_string}'")

# Convert to lowercase and remove non-alphanumeric characters
filtered = ""
for ch in s:
    if ch.isalnum():
        filtered += ch.lower()

# Check palindrome
if filtered == filtered[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

