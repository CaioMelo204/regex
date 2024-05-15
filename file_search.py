import re

with open("sample1.txt", "r") as f:
    for line in f:
        match = re.search("sample", line)
        if match: 
            print(f'found match in line: ', line)
            break 