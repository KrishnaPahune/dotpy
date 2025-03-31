import re

text = '''
This is a test. A simple test for a regex pattern.'''

pattern = r"\ba\b"

# match = re.search(pattern,text)

# if match:
#     print(f"Match found at index {match.start()} - {match.end()}: {match.group()}")
# else:
#     print("Match not found")

matches = list(re.finditer(pattern, text))

if matches:
    print(f"Found {len(matches)} occurrences of 'Data':\n")
    for match in matches:
        print(f"Match found at index {match.start()} - {match.end()}: {match.group()}")
else:
    print("Match not found")