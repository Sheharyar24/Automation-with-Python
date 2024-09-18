'''Extracting numbers from websites (UAE numbers only!)'''

import re
import pyperclip

# Load the content that we copied from the website
contents = pyperclip.paste()

# Create a regex object/pattern for the phone numbers to match
phoneNum = re.compile(r'\+?971\s?\d{1,2}\s?\d{3}\s?\d{4}')
teleNum = re.compile(r'06|\d{3}\s?\d{3}\s?\d{4}')

# Create a regex object/pattern for emails
mail = re.compile(r'\w*@\w*\.\w+')

# create an empty list
matches = []

matches1 = phoneNum.findall(contents)
matches2 = teleNum.findall(contents)
matches3 = mail.findall(contents)

matches += matches1 + matches2 + matches3

# Remove the duplicate values
matches = list(set(matches))

# Print the numbers found
for match in matches:
    print(match)

# Copies the final values back to the clipboard
content = pyperclip.copy(matches)
