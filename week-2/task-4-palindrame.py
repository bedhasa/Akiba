word = input("Enter a word: ")

# Challenge: make everything lowercase so "Madam" and "madam" are treated the same
word = word.lower()

is_palindrome = True
left = 0                 # start at the first letter
right = len(word) - 1    # start at the last letter

# Compare the outer letters, then move toward the middle
while left < right:
    if word[left] != word[right]:
        is_palindrome = False
        break
    left = left + 1
    right = right - 1

if is_palindrome:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")