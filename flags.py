import re

pattern = r'hello'
text = 'Hello world!!'

match = re.search(pattern, text, re.IGNORECASE)

if match:
        print("Found A match")
else:
    print("No match found")
    
