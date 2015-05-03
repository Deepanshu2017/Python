"""This program is to check what happens if we don't indent if block"""

people = 20
cats = 30
dogs = 15

if people < cats:
    print "Too many cats! World is doomed"

if people > cats:
    print "World is now even in more danger"

if people < dogs:
    print "Dogs are too much uhhh! :("

if people > dogs:
    print "YES YES YES"

dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."

if people == dogs:
    print "People are dogs."

#Now lets check our aim
"""
a = 5
b = 6
if a > b :
print "FIRST CALL SHOULD BE EXCUTED EVEN THE CONDITION IS FALSE"

if a < b:
print "SECOND CALL SHOULD BE EXCUTED EVEN THE CONDITION IS TRUE"

SO THIS SHOWS ERROR: IndentationError: expected an indented block
"""
