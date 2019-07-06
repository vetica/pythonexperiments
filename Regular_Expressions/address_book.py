import re

names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()

# print(re.match(r'Love', data))
# print(re.search(r'Kenneth', data))
# print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data))
# print(re.findall(r'\w*, \w+', data))

# print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))
# print(re.findall(r'[trehous]{9}\b', data, re.I))

# print(re.findall(r'''
#       \b@[-\w\d.]* # First a word boundary, an @, and then any number of characters
#      [^gov\t]+  # Ignore 1+ instances of the letters 'g', 'o', or 'v' and a tab
#     \b  # match another word boundary
#    ''', data, re.VERBOSE |))

# print(re.findall(r'''
#     \b[-\w]* #Find a word boundary, 1+ hyphens or characters, and a comma
#     \s  #find 1 whitespace
#     [-\w ]+  #1+ hyphens and characters and explicit spaces
#     [^\t\n] #Ignore tabs and newlines
#     ''', data, re.X))

line = re.compile(r'''
    ^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))\t #last and first names
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t #email
    (?P<phone>\(?\d{3}\)?\s?-?\d{3}-\d{4})?\t #phone number
    (?P<job>[\w\s]+,\s[\w\s.]+)\t? #job and company
    (?P<twitter>@[\w\d]+)?$ #twitter
''', re.X | re.M)

#print(line.search(data).groupdict())

for match in line.finditer(data):
    print('{first} {last} <{email}>'.format(**match.groupdict()))
