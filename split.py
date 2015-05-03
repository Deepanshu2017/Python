"""See usage of split here split(str,num) str is the delemiter which means
your script will split the sentence whenever it see 'str' in senetence
by default it is whitespace. Now num is the number in which sentence will
be seprated num 1 means sperate in 2 parts while num 3 means seprate in 4 
parts.
This is the general syntex of split method
str.split(str="", num=string.count(str)).
"""

sent = "This is my sentence line1 \n line2 \n line3"
print sent

print
print sent.split("s")
print
print sent.split()
print
print sent.split(' ',1)
