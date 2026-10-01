# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

# Hint: You can use .isalpha() to check if a character is a letter.

# hi i had to do some googling for this one bc i was lost
def counting_vowels_and_consonants(string):
    vowels = "AaEeIiOoUu"
    num_vowels = 0
    num_consonants = 0
    for character in string:
        if character.isalpha(): # checks if char is a letter
            if character in vowels:
                num_vowels += 1 # adds to num vowels if necessary until end of the string
            else:
                num_consonants += 1 # otherwise will add to consonants
    return(num_vowels, num_consonants)
print(counting_vowels_and_consonants("hello there"))
print(counting_vowels_and_consonants("My name is Omika"))



    

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

def average_vowels_and_consonants(paragraph):
    passage = paragraph.splitlines() # separates lines
    sentences = len(passage) # will display length of each sentence/line

    vowels_sentences = 0
    consonants_sentences = 0
    for sentence in passage:
        vowels, consonants = counting_vowels_and_consonants(sentence) # uses the fxn from other question
        vowels_sentences += vowels
        consonants_sentences += consonants
    average_vowels = vowels_sentences/sentences
    average_consonants = consonants_sentences/sentences
    return(sentences, average_vowels, average_consonants)


# Here is your paragraph to analyze. It is a quote from Richard Feynman. 

paragraph = """Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough."
    "Work as hard and as much as you want to on the things you like to do the best."
    "Don't think about what you want to be, but what you want to do."
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
"""
print(average_vowels_and_consonants(paragraph)) # prints (7, 19.57, 31.29) 

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph.