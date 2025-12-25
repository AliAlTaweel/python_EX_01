#Exrecise 2

# Build a simple text analyzer. Problem: Write a function count_words(text) that:
# Accepts a paragraph of text
# Returns a dictionary where keys are words and values are how many times they appeared 
# (case-insensitive)
# Example input: | text = "AI is the future. The future is now."
# Expected Output: {'ai': 1, 'is': 2, 'the': 2, 'future': 2, 'now.': 1}

"""
print("Exercise 2")
import re
def count_words(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    words = text.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

text = "AI is the future. The future is now."
print(count_words(text))
input("Press Enter to exit...")
"""