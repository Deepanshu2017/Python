# This is a example of multiple inheritance!
# If you are passing different parameters to a method being called via super
# all the implementations of that method going up the MRO towards object() need
# to have compatible signatures.
# Your classes must all accept the same arguments if you want to use
# cooperative subclassing with multiple inheritance.

class Machine:

    def __init__(self, **kwargs):
        print(kwargs.pop('processor'))
        print('I am in Machine class')

class Computer(Machine):

    def __init__(self, **kwargs):
        processor = kwargs.pop('processor')
        name = kwargs.pop('name')
        # Note here even though name is not used in base class but still we
        # have to pass it
        # This is just to make sure that signature is same from most derived
        # class to up to base class
        super().__init__(processor=processor, name=name)
        print(processor, name)
        print('I am in Computer class')

class Laptop(Machine):

    def __init__(self, **kwargs):
        processor = kwargs.pop('processor')
        name = kwargs.pop('name')
        # Note here even though name is not used in base class but still we
        # have to pass it
        # This is just to make sure that signature is same from most derived
        # class to up to base class
        super().__init__(processor=processor, name=name)
        print(processor, name)
        print('I am in Laptop class')

class Respbarry(Computer, Laptop):

    def __init__(self, **kwargs):
        processor = kwargs.pop('processor')
        name = kwargs.pop('name')
        super().__init__(processor=processor, name=name)
        print(processor, name)
        print('I am in Respbarry class')

if __name__ == '__main__':
    m = Machine(processor = 'P4')
    print()
    c = Computer(processor = 'i3',name = 'Deepanshu-PC')
    print()
    l = Laptop(processor = 'i7', name = 'Friend-Laptop')
    print()
    print(Respbarry.mro())
    print()
    r = Respbarry(processor = 'Dual-Core', name = 'Banana-pro')
