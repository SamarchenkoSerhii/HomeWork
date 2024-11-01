
name = "Alex"
time = 50


def say_hi(name, time):
#  return f"Hi. My name is {name} and I'm {age} years old"
  return f"Hi. My name is {name}, my experience as a programmer is {time} seconds"

print(say_hi(name,time))
assert say_hi("Alex", 32) == "Hi. My name is Alex, my experience as a programmer is 32 seconds", 'Test1'
assert say_hi("Frank", 58) == "Hi. My name is Frank, my experience as a programmer is 58 seconds", 'Test2'
print('ОК')