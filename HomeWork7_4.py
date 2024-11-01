elementrange = 1

def common_elements(elementrange):
    list1 = []
    for elementrange in range(0,100):
        if elementrange % 5 == 0:
            print(elementrange)
    return elementrange

print(common_elements(elementrange))

#assert common_elements() == {0, 75, 45, 15, 90, 60, 30}