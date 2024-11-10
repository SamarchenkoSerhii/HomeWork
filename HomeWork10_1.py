def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    print(begin)
    print(end)
    begin = func(begin)



    yield begin


from inspect import isgenerator

gen = some_gen(2, 4, pow)
print(next(gen))
print(next(gen))
print(next(gen))


#assert isgenerator(gen) == True, 'Test1'
#assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')
