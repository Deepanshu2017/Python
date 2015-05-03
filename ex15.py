from sys import argv
script,file_name = argv

txt = open(file_name)
prompt = "> "
print "Now I am going to show you the content of your file"
print txt.read()
print "Now enter new file name"
txt_again = raw_input(prompt)
file = open(txt_again)
print file.read()
txt.close()
file.close()
