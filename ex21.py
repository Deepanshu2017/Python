def add(var1,var2):
    return (var1 + var2)

def sub(var1,var2):
    return (var1 - var2)

def mult(var1,var2):
    return (var1 * var2)

def div(var1,var2):
    return (var1 / var2)

print add(12,6)
print sub(12,6)
print mult(12,6)
print div(12,6)
print
print add(12,sub(12,mult(12,div(12,6)))) 
