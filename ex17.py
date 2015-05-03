from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file,to_file)

#in_file = open(from_file)
#indata = in_file.read()
#If you want to open a file like this below then you don't have to close that file!
indata = open(from_file).read()

print "Input file is %d bytes long " % (len(indata))

print "Does the output file exists %r " % (exists(to_file))
print "Enter RETURN to continue else enter CTRL + C"
raw_input()
out_file = open(to_file,'a+')
out_file.write(indata)

out_file.close()
#in_file.close()
