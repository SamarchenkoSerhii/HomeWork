def find_unique_value(some_list):
    indexList = 0
    boollist = False
    def unique_number(some_list,indexList):
        boollist = True
        for i in range(0,len(some_list)):
            if some_list[i] == some_list[indexList] and indexList != i: boollist = False
        return boollist

    while (indexList < len(some_list)) and (boollist != True) :
        boollist = unique_number(some_list,indexList)
        if not boollist :  indexList += 1
    return some_list[indexList]

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
