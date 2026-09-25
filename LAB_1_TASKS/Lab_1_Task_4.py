#   4. Write a Python program to check whether the entered word is a palindrome or not.

word = input("Enter a word: ")

if word == word[::-1]:
    print("The entered word is a palindrome!")
else:
    print("The entered word is not a palindrome!")