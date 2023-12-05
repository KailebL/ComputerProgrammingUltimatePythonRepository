def is_alliteration(word1, word2):
    letter1 = "1"
    letter2 = "2"
    if word1[0] == word2[0]:
        return True
    else:
        return False






def count_vowels(word):
    vowelCount = 0
    for letter in word:
        if letter in "aeiou":
            vowelCount = vowelCount + 1
    return vowelCount
        





def count_numbers(string):
    numCount = 0
    for character in string:
        if character in "1234567890":
            numCount = numCount + 1
    return numCount






def count_target_letters(word, character):
    count = 0
    for letter in word:
        if letter in character:
            count = count + 1
    return count






def in_alphabetical_order(word):
    total = 0
    lastLetter = "1"
    for letter in word:
        if letter > lastLetter:
            lastLetter = letter
            total = total + 1
    if total == len(word):
        return True
    else:
        return False