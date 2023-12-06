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
    




def alternate_case(word):
    returnString = ""
    upcase = True
    for letter in word:
        if upcase == False:
            returnString = returnString + letter
            upcase = True
        elif upcase == True:
            returnString = returnString + letter.upper()
            upcase = False
    return returnString





def remove_vowels(string):
    returnString = ""
    for letter in string:
        if letter not in ["a", "e", "i", "o", "u"]:
            returnString = returnString + letter
    return returnString






def to_camel_case(string):
    returnString = ""
    lastSpace = False
    for letter in string:
        if letter == " ":
            lastSpace = True
        elif lastSpace == True:
            returnString = returnString + letter.upper()
            lastSpace = False
        else:
            returnString = returnString + letter
    return returnString






def to_snake_case(phrase):
    returnString = ""
    for letter in phrase:
        if letter == " ":
            returnString = returnString + "_"
        else:
            returnString = returnString + letter
    return returnString






def without_duplicates(integers):
    returnList = []
    lastNum = 0
    for number in integers:
        if number == lastNum:
            lastNum = number
        elif number != lastNum:
            returnList.append(number)
            lastNum = number
    return returnList





def filter_valid_act_scores(integers):
    returnList = []
    for number in integers:
        if number >= 1 and number <= 36:
            returnList.append(number)
        else:
            pass
    return returnList