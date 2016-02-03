class Foo:

    def simplemethod(self): # bound method callable with object only
        print('I am in simple method')
        print(self)

    """
    bound method callable with object as well as class name
    generally used in factory style object creation
    """
    @classmethod
    def classmethod(cls):
        print('I am in class method')
        print(cls)

    """
    function and does not bounded, can be called with class as well as object
    """
    @staticmethod
    def staticmethod():
        print('I am in static method')

if __name__ == '__main__':
    f = Foo()
    f.simplemethod()
    print(f.simplemethod)
    print()
    f.classmethod()
    Foo.classmethod()
    print(f.classmethod)
    print(Foo.classmethod)
    print()
    f.staticmethod()
    Foo.staticmethod()
    print(f.staticmethod)
    print(Foo.staticmethod)
    print()
