
import re

def is_palindrome(txt):
    return txt == txt[::-1]

pattern = re.compile(r'[\s?!,.;:\d\\]+')
#pattern.sub
#turlog

if __name__ == "__main__":

    while True:
        word = input("Podaj słowo: ")
        if not word:
            break
        print(is_palindrome(pattern.sub('' , word).lower()))
