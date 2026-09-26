#   3. Read a text file, count word frequencies, and display the five most frequent words.

text = """Python is a programming language.
Python is easy to learn.
Python is used for data science.
Programming with Python is fun."""

with open("sample.txt", "w") as file:
    file.write(text)

print("sample.txt saved successfully!")

with open("sample.txt", "r") as file:
    text = file.read()

words = text.lower().split()

word_count = {}

for i in words:
    if i in word_count:
        word_count[i] += 1
    else:
        word_count[i] = 1

print(word_count)