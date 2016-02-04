# def Foo(func):
#     def inner():
#         print(30 * '*')
#         func()
#         print(30 * '*')
#         return
#     return inner
#
# def Bar():
#     print('I am in bar')
#
# """
# By putting @function_name we are make Foo as a decorator function of Baz
# so Baz is equivalent to
# Baz = Foo(Baz)
# """
# @Foo
# def Baz():
#     print('I am in buz')
#
# if __name__ == '__main__':
#     Bar = Foo(Bar)
#     Bar()
#     Baz()

#####################################################################

# def smart_div(func):
#     def div(a, b):
#         if b == 0:
#             return 'cannot divide'
#         return func(a, b)
#     return div
#
# @smart_div
# def m_div(a, b):
#     return a / b
#
# if __name__ == '__main__':
#     print(m_div(2, 3))
#     print(m_div(4, 2))
#     print(m_div(4, 0))

#####################################################################

def pound_sign(func):
    def inner(msg):
        print('#' * 30)
        func(msg)
        print('#' * 30)
        return
    return inner

def dollar_sign(func):
    def inner(msg):
        print('$' * 30)
        func(msg)
        print('$' * 30)
        return
    return inner

"""
writing below is equivalent to
printer1 = pound_sign(dollar_sign(printer1))
"""

@pound_sign
@dollar_sign
def printer1(msg):
    print(msg)

@dollar_sign
@pound_sign
def printer2(msg):
    print(msg)

if __name__ == '__main__':
    printer1('text')
    print()
    printer2('text')
