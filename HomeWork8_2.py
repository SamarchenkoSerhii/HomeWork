def is_palindrome(text):
    text1 = ""
    resulttest = True
    for i in range(len(text)):
        if text[i].isalnum() :
            text1 = text1 + text[i]
    text1 = text1.lower()
    for i in range(len(text1)):
        if text1[i] != text1[(len(text1)-1-i)]:
            resulttest = False
    return resulttest

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")