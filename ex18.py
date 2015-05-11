
def print_two(*args):
    argv1, argv2 = args
    print "argv1: %s  argv2: %s" % (argv1,argv2)
    print args[0]
    #args[0] = str("Deepanshu")
    # To do the above read article on this link and you will never do this type of stupid things again
    #http://www.jeffknupp.com/blog/2012/11/13/is-python-callbyvalue-or-callbyreference-neither/
    """Also '*' before argument name in function means that this function can take more then 2 argument and all arguments will be assigned to that name after * as a tuple as in above code args will contain a tuple"""

def print_two_again(zed,show):
    print "argv1: %s  argv2: %s" % (zed,show)

def print_one(argv):
    print "argv1: %s" % (argv)

def print_none():
    print "Nothing to print"

zed = "zed"
show = "show"
print_two(zed,show)
print_two_again(zed,show)
print_one("zed")
print_none()
print zed

"""
some_guy = 'Fred'

first_names = []
first_names.append(some_guy)

another_list_of_names = first_names
another_list_of_names.append('George')
some_guy = 'Bill'

print (some_guy, first_names, another_list_of_names)
"""
