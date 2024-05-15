import re

def return_match(match):
    if match:
        print("Found A match")
    else:
        print("No match found")

# Search (Search the pattern inside the string)
text = "This is a sample text"
pattern = 'sample'

return_match(re.search(pattern, text))
                               
# Match (Search the pattern in the beggining of the string)
text = "This is a sample text"
pattern = 'This'

return_match(re.match(pattern, text))

# FullMatch (match if the entire string match the pattern)

text = "2023-03-11"
pattern = r'\d{4}-\d{2}-\d{2}'

return_match(re.match(pattern, text))

# Findall 

pattern = r'\d+'
text = "The price of the book is $19.50"

matches = re.findall(pattern, text)

print(matches)


# Sub and Subn
pattern = r'\b\w{4}\b'
text = "The quick brown fox jumps over the lazy dog"

new_text = re.sub(pattern, '****', text)

print(new_text)

#split 

pattern = r'\s+'
text = "The quick brown fox jumps over the lazy dog"

words = re.split(pattern, text)

print(words)

