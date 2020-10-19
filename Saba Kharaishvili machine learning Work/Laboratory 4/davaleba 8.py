list1 = [2, 123, 43, 7, 5, 44, 33, 13]
list2 = [1, 93, 43, 34, 25, 44, 783, 33]
def common(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y :
                result = True
                return result

print(common(list1,list2))
