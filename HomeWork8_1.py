
def add_one(some_list):
    some_number = ""
    def str_to_list(some_number):
        some_list = []
        for i in range(0, len(some_number)): some_list.append(int(some_number[i]))
        return some_list

    for i in range(0,len(some_list)):
        some_number = some_number + str(some_list[i])
    some_number = str(int(some_number) + 1)
    return str_to_list(some_number)


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'

print("ОК")