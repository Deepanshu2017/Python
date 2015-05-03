# Exercise 8 for LPTHW

formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (True,False,True,False)
print formatter % (
                   "This is a line one, ",
                   "This is a line two, ",
                   "This is a line three, ",
                   "This is a line four, "
                   )