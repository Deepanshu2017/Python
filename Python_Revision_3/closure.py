# Closure
def outer(var1):
    def inner(var2):
        return var1 * var2
    return inner

if __name__ == '__main__':
    make3 = outer(3)
    make5 = outer(5)
    print(make3(9)) # 3 * 9 = 27
    print(make5(4)) # 5 * 4 = 20
    print(make3.__closure__[0].cell_contents)
    print(make5.__closure__[0].cell_contents)
    # print(make3.__closure__[1].cell_contents) # tuple index out of range
