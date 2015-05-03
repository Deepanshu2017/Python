# -*- coding: utf-8 -*-

""" This program will tell you about the difference between str() function
and repr() function. Basically repr() function is use for debugging"""

import datetime

d = datetime.date.today()

# str() function
print str(d)

# repr() function
print repr(d)

var_str = str(d)
var_repr = repr(d)

# how str variable should be printed
print '%s' % var_str

# how repr variable should be printed
print '%r' % var_repr

