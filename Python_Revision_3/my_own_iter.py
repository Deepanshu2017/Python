class PowOfTwo:
    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

if __name__ == '__main__':
    obj1 = PowOfTwo(4)
    for itr in obj1:
        print(itr)

    obj2 = PowOfTwo(4)
    itr = iter(obj2)
    print(next(itr))
    print(next(itr))
    print(next(itr))
    print(next(itr))
    # print(next(itr)) # StopIteration exception
