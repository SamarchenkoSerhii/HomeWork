import string
StringToGO  =  input("Specify the `a-Z` interval from the alphabet: ")
IndexBegin = string.ascii_letters.index(StringToGO[0])
IndexEnd = string.ascii_letters.index(StringToGO[2])
ABCList = string.ascii_letters

if IndexEnd > IndexBegin :
    print(ABCList[IndexBegin:IndexEnd+1])
else:
    print(ABCList[IndexEnd:IndexBegin+1])