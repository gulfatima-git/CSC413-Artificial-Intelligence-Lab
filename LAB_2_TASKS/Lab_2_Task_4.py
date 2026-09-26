#   4. Modify the program to handle invalid input and missing files using try-except.

text = """Python is a programming language.
Python is easy to learn.
Python is used for data science.
Programming with Python is fun."""

with open("sample.txt", "w") as file:
    file.write(text)

print("sample.txt saved successfully!")

try:
    filename = input("Enter the file name: ")

    with open(filename, "r") as file:
        text = file.read()

    words = text.lower().split()

    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    sorted_words = sorted(
        word_count.items(),
        key=lambda x: x[1],
        reverse=True
    )

    print("\nFive most frequent words:")

    for word, frequency in sorted_words[:5]:
        print(f"{word}: {frequency}")

except FileNotFoundError:
    print("Error: The file was not found.")

except ValueError:
    print("Error: Invalid input.")

except Exception as e:
    print("An unexpected error occurred:", e)
