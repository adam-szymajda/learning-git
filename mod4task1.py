word = input("Podaj słowo: ")

def is_palindrome(txt):
    return txt == txt[::-1]

print(is_palindrome(word))
