import re
import os

str = 'an example word:cat!! word:cat'
match = re.search(r'word:\w\w\w', str)
# If-statement after search() tests if it succeeded
TESTER = re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$")
if match:
    print ( 'found', match.group())## 'found word:cat')
else:
    print( 'did not find')



if __name__ == "__main__":
    val = range(1,5)
    print(*val)
    val2 = None
    print(val2)

    str ="this is first exapme"

    for a in str:
        print ("a"+a)
        any(a)
        a.isalnum()
    strArr= str.split(" ")
    str = ("_").join(strArr)
    str1 ="this123491"
    for i in range(0,len(str1),4):
        print(i)
    print(dir(os))