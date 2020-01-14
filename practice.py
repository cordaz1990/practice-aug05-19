#Aliasing

>>> a = [1,2,3]
>>> b = a
>>> b is a
True

>>> letters = ['a','b','c']
>>> delete_head(letters)
>>> letters
['b','c']

t1 = [1,2]
t2 = t1.append(3)
>>>t1
[1,2,3]
>>> t2
None
