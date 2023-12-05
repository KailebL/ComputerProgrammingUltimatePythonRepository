def count_failing_grades(grades):
    failCount = 0
    for number in grades:
        if number < 60:
            failCount = failCount + 1
    return failCount

print("failing ---->", count_failing_grades([20, 80, 70, 90, 40])) #2




def count_act_scores(scores):
    validScoreCount = 0
    for number in scores:
        if number >= 1 and number <= 36:
            validScoreCount = validScoreCount + 1
    return validScoreCount

print("count act ---->", count_act_scores([20, 30, 40])) #2




def number_sum(numbers):
    sum = 0
    for number in numbers:
        sum = sum + number
    return sum

print("sum? ---->", number_sum([20, 30, 40])) #90
print("sum? ---->", number_sum([5, 1, 2])) #8





def average_act_score(scores):
    if len(scores) != 0:
        validCount = 0
        validSum = 0
        for number in scores:
            if number <= 36 and number >= 1:
                validCount = validCount + 1
                validSum = validSum + number
        if validSum != 0 or validCount != 0:
            return validSum / validCount




def all_true(bool_list):
    check = 0
    for value in bool_list:
        if value == True:
            check = check + 1
    if check == len(bool_list):
        return True
    else:
        return False

print("all true? ---->", all_true([True, True, False])) #false
print("all true? ---->", all_true([True, True, True])) #true
print("all true? ---->", all_true([False, False, False])) #false
    
        



def any_true(booleanList):
    if len(booleanList) == 0:
        return False
    else:
        for value in booleanList:
            if value == True:
                return True
            else:
                return False
        
print("any true? ---->", any_true([True, False, False])) #true
print("any true? ---->", any_true([True, True, True])) #true
print("any true? ---->", any_true([False, False, False])) #false






def mostly_true(booleanList):
    if len(booleanList) != 0:
        trueCount = 0
        for value in booleanList:
            if value == True:
                trueCount = trueCount + 1
        if trueCount >= len(booleanList) / 2:
            return True
        else:
            return False
    else:
        return False
    
print("mostly true? ---->", mostly_true([True, False, True])) #true
print("mostly true? ---->", mostly_true([True, False, False])) #False
print("mostly true? ---->", mostly_true([False, False, False])) #False




def has_vowel(lettersList):
    vowelCount = 0
    if len(lettersList) != 0:
        for letter in lettersList:
            if letter in ["a", "e", "i", "o", "u"]:
                vowelCount = vowelCount + 1
        if vowelCount > 0:
            return True
        else:
            return False
    elif len(lettersList) == 0:
        return False
    




def all_the_same(numbers):
    lastNum = 0
    allsame = False
    for number in numbers:
        if number == lastNum:
            allsame = True
            lastNum = number
        elif len(numbers) == 1:
            allsame = True
        else:
            allsame = False
            lastNum = number
    return allsame

    




def increasing(integers):
    lastNumber = 0
    if len(integers) < 2:
        return False
    else:
        for number in integers:
            if number > lastNumber:
                return True
                lastNumber = number
            else:
                return False
            



        
def is_incrementing(numbers):
    lastNumber = 0
    if len(numbers) == 0:
        return False
            





def has_adjacent_repeat(numbers):
    numList = []
    repeat = False
    if len(numbers) > 0:
        for number in numbers:
            numList.extend(number)
            if number in numList:
                repeat = True




def sum_with_skips(integers):
    ignore = False
    sum = 0
    for number in integers:
        if number == -1 and ignore == False:
            ignore = True
        elif number == -1 and ignore == True:
            ignore = False
        elif ignore == False and number != -1:
            sum = sum + number
    return sum