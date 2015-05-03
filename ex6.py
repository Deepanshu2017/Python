# Exercise 6 of Learning Python The Hard Way (LPTHW)

x = "there are %d types of people" % (10)

binary = "Binary"
do_not = "do_not"

y = "those who knows %s and those who %s" % (binary,do_not)

print x
print y

print "I said: %r" % (x)
print "I also said: '%s' ." % (y)

hilarious = False
joke_evaluation = "Isn't that joke so funny? %r"

# Now See magic

print joke_evaluation % hilarious

w = "This is a left side of ..."
e = "a string with right side."

print w + e

