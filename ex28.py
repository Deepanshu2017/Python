""" As we all know there are many boolen operaters in Python :D but this article consist a surprise
operater which I though will never work but it works :D :D :D I am typing this and I am also shoked :-/ """




print (1 == 3 and 1 == 1)  #This will return ? Ofcourse False
print (1 == 2)             #This will return False
print (1 == 1)             #This will return 1 instead of True

#read this

""" The expression x and y first evaluates x; if x is false, its value is returned; otherwise, y is evaluated 
and the resulting value is returned.

    The expression x or y first evaluates x; if x is true, its value is returned; otherwise, y is evaluated 
and the resulting value is returned.

(Note that neither and nor or restrict the value and type they return to False and True, but rather 
return the last evaluated argument. This is sometimes useful, e.g., if s is a string that should be replaced 
by a default value if it is empty, the expression s or 'foo' yields the desired value. Because not has to 
invent a value anyway, it does not bother to return a value of the same type as its argument, so e.g., 
not 'foo' yields False, not ''.)

>>> "test1" and "test2"
'test2'
>>> "" and "test2"
''
>>> "" or "test2"
'test2'
>>> "test1" or "test2"
'test1'

In "test1" and "test2" case, test1 is evaluated and it turns out to be Truthy. (Becasue "test1" is non empty 
string) So, the second expression also has to be evaluated and the result of that evaluation 
is returned as test2.

In the "" and "test2" case, since empty strings are Falsy, and need not have to check the second expression.

In "" or "test2", since the empty strings are Falsy, or evaluates the next expression and returns that 
as the result. Hence, test2.

In "test1" and "test2", since test1 is Truthy (Non empty string), or need not have to evaluate the 
second expression and returns test1.

"""


print 1 or 2
print 1 and 2

#Last but not the least
print 5 != 4
print 5 <> 4

#YES <> is equivelent to != HAHA!! That's why Python is a kind of Snake. YOU KNOW WHAT I MEAN ;)
