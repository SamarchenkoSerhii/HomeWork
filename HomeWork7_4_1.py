def common_elements():
    List1 = []
    List2 = []
    for i in range(0, 100):
        if i % 3 == 0: List1.append(i)
        if i % 5 == 0: List2.append(i)
    List1 = set(list(set(List1) & set(List2)))
    return List1

print(common_elements())
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
