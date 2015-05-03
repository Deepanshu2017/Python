"""Here what I am doing is going to pratice the major concepts which I have learned
till now"""

from sys import argv

#Print something
print "Python is a very powerful language"

#add +
#subtract -
#divide /
#multiply *
#modules %
#power **
print ((2+3*2-3/5) % 100 ) ** 3

#logical and
#logical or
#logical not
#logical expression order NOT > AND > OR
print 1 == 3 or 2 == 4 or not(1 == 2 and 2 == 2)

#String Concatenation!
string1 = "This is an example"
string2 = " "
string3 = "of string concatenation."
string4 = string1 + string2 + string3
print string1 + string2 + string3
print string4

#let's now look at methods
def my_method(argv):
    """This will become the help document to run this type import file name and the help file name
    by the way %s is used for print the string as it is while %r is basically used for debugging %r will print
    non-printable charcter too!"""
    print "You pass %r argument" % (argv)
    print "This is with %s with same argument" % (argv)

#Method calling
my_method("Welcome to the jungle \t*****")

#Now lets move on to some file handling
#I am going to create a new file called python_pratice_file.txt
#too long name so I am going to take it in variable
name = 'python_pratice_file.txt'
file_name = open(name,'w')
file_name.write(raw_input("> "))
file_name.write('\n')
file_name.write(raw_input("> "))
file_name.write('\n')
file_name.write(raw_input("> "))
file_name.write('\n')
file_name.close()

#now show the content of the file you have created and closed it
file_name = open(name,'r')
#print whole file at once
print file_name.read()

#Now the head pointer or courser is at the EOF character of file so we have to rewind our file
file_name.seek(0)
#Remember we have used "readlines" instead or "readline" See this carefully
for line in file_name.readlines():
     print line,

file_name.close()

#We can use "with open(name,'w') as file_name" and we don't have to close that file

#now lets move on to lists
#also I will use split,join and replace methods
#Systex of an empty list
words = []
words2 = []
with open(name,'r') as file_name:
    data = file_name.readlines()
    for line in data:
        data = line.split(' ')
        words.append(data)
        for i in data:
            words2.append(i)
print words
print words2

#now join
string_words = ""
for i in words2:
    global string_words
    string_words = str(string_words) + str(i) + " "

temp_list = string_words.split('\n')

print string_words
#now replace method
print string_words.replace('\n',' ')
print temp_list
final_list = ""
for i in temp_list:
    global final_list
    final_list = final_list + str(i) + " "

print final_list


#now We have studied about join,split and replace methods list
#Now work lets with command line argument for that we have to import sys module

script_name, first, second = argv
print first + second

#now lets work with if-elif-else

if (first + second) <= 2:
    print "I am in IF"
elif (first + second) <= 10:
    print "I am in elif"
else:
    print "I am in else"

#now I will show you for-else loop
for i in range(0,5):
    if i == 4:
        print "IF THIS EXCUTES"
        break
    print i
else:
    print "THEN THIS WILL NOT EXCUTE"

print "\v\v\v\v\v\v"

#Now while-else loop
while i < 20:
    if i > 40:
        print "IF THIS DOES NOT EXCUTE "
        break
    print i
    i += 8
else:
    print "THEN THIS WILL EXCUTE"

this_is_dict = {"one":"1","two":"2","three":"3","four":"4","five":"5"}
for key,value in this_is_dict.items():
    print key,
    print this_is_dict[key]

print this_is_dict.get("five","Does not exists")
print this_is_dict.get("six","Does not exists")
this_is_dict.setdefault("six","6")
print this_is_dict.get("six","Does not exists")


print "\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v"

#Now finally move on to classes

class Animal(object):
    pass #pass is a place holder means we can leave this class for future use and without even adding code in it


"""

We will talk about this type of inhertance later :(

class machine(object):
    def __init__(self,processor):
        print "I am in contructor of machine class"
        print processor

class computer(machine):
    def __init__(self,name,processor):
        print "I am in contructor of computer class"
        super(computer,self).__init__(processor)
        print name,
        print processor

class laptop(machine):
    def __init__(self,name,processor):
        print "I am in contructor of laptop class"
        super(laptop,self).__init__(processor)
        print name,
        print processor

class respbarry(computer,laptop):
    def __init__(self,name,processor):
        print "I am in contructor of respbarry class"
        super(respbarry,self).__init__(name,processor)
        print name,
        print processor

m = machine("P4")
c = computer("Computer","P4")
l = laptop("Laptop","P4")
r = respbarry("Respbarry","P4")

"""


class base(object):
    argv = 5
    def __init__(self,argv1):
        self.argv1 = argv1
    def print_vales(self):
        argv1 = raw_input("> ")
        print argv1
        print base.argv
        base.argv += 10
        print base.argv

a = base(5)
a.print_vales()
a.print_vales()


class derived(base):
    argv2 = 10
    def __init__(self,value):
        self.value = value
    def get_value(self):
        derived.argv2 = int(raw_input("> "))
        self.value = int(raw_input("> "))
        print self.value
        print derived.argv2

b = derived(6)
b.print_vales()
b.get_value()
