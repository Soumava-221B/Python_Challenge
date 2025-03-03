"""
Python Code Challenge #3: Sort a String
Your goal is to implement a function, sort_words(), that takes a string containing one or more words separated by spaces as the input argument and returns a string containing those words sorted alphabetically.

Example Test Output
>>> sort_words('banana ORANGE apple')
'apple banana ORANGE'
"""

# def sort_words(sentence: str) -> str:
#     """
#     Takes a string containing one or more words separated by spaces
#     and returns a string with words sorted alphabetically.
#     """
#     words = sentence.split()
#     sorted_words = sorted(words)
#     return " ".join(sorted_words)

# # Example usage
# input_sentence = "banana apple orange grape"
# print(sort_words(input_sentence))


def sort_sentence(phrase):
    return ' '.join(sorted(phrase.split(), key=str.casefold))

if __name__ == '__main__':
    print(sort_sentence('banana Orange apple'))