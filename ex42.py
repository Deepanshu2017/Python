## Animal is-a object
class Animal(object):
    pass

## Dog is a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Animal has a name (this is a contructor)
        self.name = name

## cat is a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
	print "I am in Person contructor"
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
	print "I am in Employee contructor"
        ## Employee has-a name and salary
        super(Employee, self).__init__(name)
        ## Employee contructor is calling the contructor of person
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is a Cat
satan = Cat("Satan")

## mary is a peron
mary = Person("Mary")

## Mary's pet name is satan which is-a cat
mary.pet = satan

## frank is a Employee who has-a name
frank = Employee("Frank", 120000)

## frank's pet name is rover
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a Salmon which is-a fish
crouse = Salmon()

## harry is-a fish
harry = Halibut()
