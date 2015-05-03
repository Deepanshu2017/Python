
ten_things = "Apples Oranges Crows Telephone Light Sugre"

print "Wait there are not exactly ten things :-/"

#Lets break our string ten_things using split function and space as delemeter [UNIX MAN ;-) ]

stuff = ten_things.split(' ')

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

#Now iterate over stuff and add items in it untill there are enough items(10)

while len(stuff) != 10:
    """This loop pop's the items from more_stuff named list and add it into stuff list"""
    next_one = more_stuff.pop()
    print "Adding %r" % (next_one)
    stuff.append(next_one)
    #End of while loop

#Print the second item from list named stuff
print stuff[1]
#print the last item from the list named stuff
print stuff[-1]
#Let's try something new
print stuff[-2]
print stuff[-5]
"""So yes it works -1 means last item and -2 means second last and -5 means 5th item from last"""

print ' '.join(stuff)
print '#'.join(stuff[3:5])

























