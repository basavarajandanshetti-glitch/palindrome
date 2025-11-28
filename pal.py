import sys

default_string = "madam"
if len(sys.argv) >= 2:
    s = " ".join(sys.argv[1:])
else:
    s = input("Enter string (press Enter for default 'madam'): ").strip()
    
   if s == "":
        print("Using default string:", default_string)
        s = default_string

filtered = ""
for ch in s:
    if ch.isalnum():
        filtered += ch.lower()
if filtered == filtered[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
