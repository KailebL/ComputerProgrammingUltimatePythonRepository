def make_abc():
    return ["a", "b", "c"]

print("--->", make_abc())





def equal_edges(list):
    if list[0] == list[-1]:
        return True
    else:
        return False
    
print("Equal Edges -->", equal_edges([1, 2, 3, 4, 1]))
print("Equal Edges -->", equal_edges([5, 6, 7, 8, 9]))
print("Equal Edges -->", equal_edges([-1, 0, 1, 2, -1]))
print("Equal Edges -->", equal_edges([4, 4]))





def common_edge(list1, list2):
    if list1[0] == list2[0] or list1[0] == list2[-1]:
        return True
    elif list1[-1] == list2[0] or list1[-1] == list2[-1]:
        return True
    else:
        return False
    
print("Common edge ---->", common_edge([1, 2, 3 ,4], [5, 6, 7, 8]))
print("Common edge ---->", common_edge([1, 2, 3], [3, 4, 5]))
print("Common edge ---->", common_edge([4, 5, 6], [7, 8, 9]))
print("Common edge ---->", common_edge([-1, 0, 1, 2, -1], [2, 3, 4, 5]))
print("Common edge ---->", common_edge([3, 3, 3], [3, 3, 3, ])) 




def all_the_same(list):
    if len(list) == 3:
        if list[0] == list[1] and list[1] == list[2]:
            return True
        else:
            return False
    else:
        return "List must have 3 values"

print("All the same ---->", all_the_same([1, 2, 3]))
print("All the same ---->", all_the_same([5, 5, 5]))
print("All the same ---->", all_the_same([-1, 0, 1]))
print("All the same ---->", all_the_same([3, 3, 3]))
print("All the same ---->", all_the_same([4, 5, 6]))




def all_unique(numberslist):
    if len(numberslist) == 3:
        if numberslist[0] != numberslist[1] and numberslist[1] != numberslist[2]:
            return True
        elif numberslist[0] == numberslist[1] and numberslist[1] == numberslist[2]:
            return False
        else:
            return False
    else:
        return "List must have 3 values"
    
print("All unique ---->", all_unique([1, 2, 3]))
print("All unique ---->", all_unique([5, 5, 5]))
print("All unique ---->", all_unique([-1, 0, 1]))
print("All unique ---->", all_unique([3, 3, 3]))
print("All unique ---->", all_unique([4, 5, 6]))




def increasing(list):
    if len(list) == 3:
        if list[0] < list[1] and list[1] < list[2]:
            return True
        else:
            return False
    else:
        return "List must have 3 values"
    
print("Increasing ---->", increasing([1, 2, 3]))
print("Increasing ---->", increasing([5, 5, 5]))
print("Increasing ---->", increasing([-1, 0, 1]))
print("Increasing ---->", increasing([3, 3, 3]))
print("Increasing ---->", increasing([4, 5, 6]))




def all_true(booleans):
    if len(booleans) == 3:
        if booleans[0] == True and booleans[0] == booleans[1] and booleans[1] == booleans[2]:
            return True
        else:
            return False
    else:
        return "List must have 3 values"
    
print("All true ---->", all_true([True, False, True]))
print("All true ---->", all_true([False, False, False]))
print("All true ---->", all_true([True, True, True]))
print("All true ---->", all_true([False, True, False]))
print("All true ---->", all_true([True, False, True]))




def mostly_true(list):
    if len(list) == 3:
        if list.count(True) >= 2:
            return True
        else:
            return False
    else:
        return "List must have 3 values"
    
print("Mostly true ---->", mostly_true([True, False, True]))
print("Mostly true ---->", mostly_true([False, False, False]))
print("Mostly true ---->", mostly_true([True, True, True]))
print("Mostly true ---->", mostly_true([False, True, False]))
print("Mostly true ---->", mostly_true([True, False, False]))




def make_copy(integers):
    if len(integers) == 3:
        return integers
    else:
        return "Must have 3 values"

print("Make copy, 5, 6, 1 ---->", make_copy([5, 6, 1]))





def repeat_thrice(integer):
    # integer = list(integer)
    # integer = []
    # integer = integer, integer, integer
    return [integer, integer, integer]

print("Repeat thrice, -1 ---->", repeat_thrice(-1))
print("Repeat thrice, 5 ---->", repeat_thrice(5))






def make_reversed_copy(listIntegers):
    listIntegers = list(listIntegers)
    copylist = listIntegers
    first = listIntegers[0]
    last = listIntegers[2]
    copylist[0] = last
    copylist[2] = first
    return copylist

print("Reversed copy, 1, 2, 3 ---->", make_reversed_copy([1, 2, 3]))
print("Reversed copy, 1, 2, 3 ---->", make_reversed_copy([13, 5, 6]))




def reverse_in_place(integers):
    first = integers[0]
    last = integers[2]
    integers[2] = first
    integers[0] = last
    return integers

print("reverse in place, 1, 2, 3 ---->", reverse_in_place([1, 2, 3]))
print("reverse in place, 13, 5, 6 ---->", reverse_in_place([13, 5, 6]))