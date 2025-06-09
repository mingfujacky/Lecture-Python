"""
sample email:
>>> Hi Leo,
>>> Dan -- any luck with your natural language research?
>>> Yes! That website you showed me https://www.kaggle.com/
>>> is very useful. I found a dataset on there that collects a lot
>>> of questions and answers that might be useful to my research.
>>> Thank you,
>>> Dan
"""
import pyperclip
# Manually copy sample email to clipboard, press Ctrl+C

# Paste text from clipboard
text = pyperclip.paste()

# Clean up each line: remove '>>>' and leading spaces
cleaned_lines = [line.replace('>>>', '').lstrip() for line in text.splitlines()]
cleaned_text = '\n'.join(cleaned_lines)

print("Cleaned email text:")
print(cleaned_text)


