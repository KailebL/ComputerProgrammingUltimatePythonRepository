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
    list = list.replace(" ", "")
    n1, n2, n3 = int(list.split(","))

print(all_the_same)