# Weekly typed variable have one underscore in front of their name
# like in our example _hiddenlist

# def _wont():
#     print('It will not auto import')
#
# class Queue:
#
#     def __new__(cls):
#         print('I am in new method of spam')
#         obj = object().__new__(cls)
#         return obj
#
#     def __init__(self):
#         print('Initilization of object')
#         self._hiddenlist = [1, 2, 3, 4, 5, 6]
#
#     def push(self, var):
#         self._hiddenlist.insert(0, var)
#
#     def pop(self):
#        return self._hiddenlist.pop(-1)
#
#     def __repr__(self):
#        return('{}'.format(self._hiddenlist))
#
# if __name__ == '__main__':
#     queue = Queue()
#     queue.push(0)
#     print(queue)
#     print(queue.pop())
#     print(queue)


class Spam:

    __egg = 7
    def __private_method(self):
        print('I am in private method')

    def print_egg(self):
        print(self.__egg)

if __name__ == '__main__':
    s = Spam()
    s.print_egg()
    print(s._Spam__egg)
    s._Spam__private_method()
