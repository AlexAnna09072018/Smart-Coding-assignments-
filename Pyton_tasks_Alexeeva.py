Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:25:23) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def add (a,b):
	return a+b

>>> a=6
>>> b=5
>>> add(a,b)
11
>>> assert add(1,3) == 4
>>> def sumOfList(someList):
    total = 0
    for i in someList:
        total = total + i
    return total

>>> numbers = [1,2,3,5]
>>> sumOfList(numbers)
11
>>> assert  sumOfList(numbers)==11

