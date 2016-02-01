# http://agiliq.com/blog/2012/06/__new__-python/
# import datetime
#
# class Foo:
#     def __new__(cls, *args, **kwargs):
#         ins = super().__new__(cls, *args, **kwargs)
#         print('I am in new')
#         ins.attr = datetime.datetime.now()
#         return ins
#     def __init__(self, *args, **kwargs):
#         print('I am in init')
#         self.x = 0
#         self.y = 0
#
# if __name__ == '__main__':
#     f = Foo()
#     print(type(f))
#     print(f.attr)


class Spam:

    def __init__(self, *args, **kwargs):
        self.x = 0
        print('init of Spam')


class Eggs:

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(Spam, *args, **kwargs)
        print('In __new__ method')
        return obj

    def __init__(self, *args, **kwargs):
        self.x = 4
        print('init of Eggs')

if __name__ == '__main__':
    e = Eggs()
    print(type(e))
    e.__init__()
    print(e.x)
