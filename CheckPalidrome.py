"""
Python Code Challenge #2: Identify a Palindrome
Your goal is to implement a function, is_palindrome(), that takes a text string as the input argument and returns a boolean indicating whether or not it's a palindrome.

Example Test Output
>>> is_palindrome('hello world')
False
>>> is_palindrome('Go hang a salami, I’m a lasagna hog.')
True
"""

import re

def check_palindrome(sentence):
    start = ''.join(re.findall(r'[a-z]+', sentence.lower()))
    end = start[::-1]
    return start == end

if __name__ == '__main__':
    print(check_palindrome('hello world'))  # false
    print(check_palindrome("Go hang a salami, I'm a lasagna hog."))  # true