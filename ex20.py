"""seek function deals with bytes not in lines and file_object.seek(bytes)
here the cursor will be on the bytes + 1 character since files first character
is seek(0) and second character is seek(1) :D (C array index concept :D :D )"""

from sys import argv

script,file_name = argv

def print_all(file):
    print file.read()

def rewind(file):
    file.seek(0)

def print_line(line,file):
    print line,file.readline(),

file = open(file_name,'r+')
print "Lets print whole file"

print
print

print_all(file)

print """Lets now rewind all like a tape so that curser can reach
         at the first charactor of the file :D """

print
print

rewind(file)

print "Lets now read line by line"
print
print

line = 1
for line in range(1,4):
	print_line(line,file)

