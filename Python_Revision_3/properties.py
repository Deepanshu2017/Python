# class Celsius:
#     def __init__(self, temperature = 0):
#         self.temperature = temperature
#
#     def to_fahrenheit(self):
#         return (self.temperature * 1.8) + 32
#
#     def get_temperature(self):
#         print("Getting temperature")
#         return self._temperature
#
#     def set_temperature(self, value):
#         print("Setting temperature")
#         if value < -273:
#             raise ValueError("temp")
#         self._temperature = value
#
#     temperature = property(get_temperature, set_temperature)
#     # syntex: property(fget = None, fset = None, fdel = None, fdoc = None)
#     # line number 18 is same as below three lines
#     # temperature = property()
#     # temperature = temperature.getter(get_temperature)
#     # temperature = temperature.setter(set_temperature)
#
# if __name__ == '__main__':
#     c = Celsius(10)
#     c.temperature = 20
#     print(c.temperature)

class Celsius:
    def __init__(self, temp = 0):
        self.temp = temp

    def to_fahrenheit(self):
        return (self.temp * 1.8) + 32

    @property
    def temp(self):
        print('Getting value')
        return self._temp;

    @temp.setter
    def temp(self, value):
        if value < -273:
            raise ValueError('temp')
        print('Setting value')
        self._temp = value

if __name__ == '__main__':
    c = Celsius(10)
    c.temp = 20
    print(c.temp)
