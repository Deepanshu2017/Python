""" Remember one thing in Python i file mode that is the position of 
    courser matters a lot. file.truncate() will truncate the file 
    form the current curser position to the end also if we pass arguments
    then it will leave the number of size in file and truncate everything.
    if you read whole file then the curser will be on the last charactor 
    means it will be on EOF charater. So curser Position MATTERS A LOT.
    
    r
    Read-only mode. The file pointer is placed at the beginning of the file.
    This is the default mode.

    r+
    Read-write mode. The file pointer will be at the beginning of the file.

    w
    Write-only mode. Overwrites the file if the file exists. If the file
    does not exist, creates a new file for writing.

    w+
    Read-write mode. Overwrites the existing file if the file exists. If the
    file does not exist, creates a new file for reading and writing.

   a
   Write-only mode. The file pointer is at the end of the file if the file
   exists. That is, the file is in the append mode. If the file does not exist,
   it creates a new file for writing.

   a+
   Read and write mode. The file pointer is at the end of the file if the file
   Exists. The file opens in the append mode. If the file does not exist, it
   creates a new file for reading and writing.
"""


from sys import argv
script, filename = argv

print "We're going to earse %r."% (filename)
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("? ")

print "Openning the file..."

target = open(filename,'r+')


print "truncating the file. Goodbye!"
print target.readline()
print target.read()
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
line4 = line1 + "\n" + line2 + "\n" + line3 + "\n"
print "I'm going to write these to file."
target.write(line4)

print "And finally, we close it"
target.close()
