import re

file_extensions = ['pdf', 'doc']

with open("sample1.txt", "r") as f:
    text = f.read()
    pattern = r'\b\w+\.(?:' + r'|'.join(file_extensions) + r')\b'
    matches = re.findall(pattern, text)
    
print(matches)