the_count = [1,2,3,4,5]
fruits = ['apple','banana','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']
for number in the_count:
    print "This is count %d" % (number)

for fruit in fruits:
    print "A fruit of type: %s" % (fruit)

for i in change:
    print "I got %r" % (i)

elements = []
for i in range(0,6):
    print "Adding %d to the list." % (i)
    elements.append(i)

for i in elements:
    print "Elements was: %d" % i

print "Now this is 2D list"
#First naive way 
item1 = []
for i in range(1,6):
    foo = []
    for j in range(1,6):
        foo.append(j)
    item1.append(foo)

#Now print this
print item1

#Now amuture way
item2 = []
for i in range(1,6):
    item2.append([foo for j in range(1,6)])

#Now print this
print item2



#Now Expert way
item3 = [[foo for i in range(1,6)] for j in range(1,6)]

#Now print this
print item3







#Now print this
print item2
