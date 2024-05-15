import re

pattern = r'(\d{4})-(\d{2})-(\d{2})'
text = 'the year is 2024-02-04'

matches = re.search(pattern, text)

if matches:
    print(matches.group(0))
    print(matches.group(1))
    print(matches.start())
    print(matches.end(0))
    print(matches.span())