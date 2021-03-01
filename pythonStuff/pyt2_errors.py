try:
    f = open('someText.txt', 'r')
    f.write("Japan")
except IOError: # for any type of error just write except:
    print("Error: Could not fint file or read data")
else:
    print("Success")
    f.close()

# finally keyword can be used instead of else
# finally keyword will be always executed

# REGULAR EXPRESSIONS
# to finad patters in text

import re # regular expressions module

patterns = ['term1', 'term2']
text = 'This is term1 text'

for pattern in patterns:
    print(pattern)
    if re.search(pattern, text):
        print("FOUNED")
    else:
        print("NOT FOUND")

match = re.search(patterns[0], text)
print(match.start())

email1 = "koluh.dinno@gmail.com"
et = "@"
print(re.split(et, email1))
# also email1.split('@')

#re.findall()

import pyt2_classes as pyt

from numpy import sin as s # use * to import everything so you dont need to use numpy.something     

print(s(3.14))

pyt.func()

# it it is directily called then __name__ = __main__, if it is called from as a module
# then __name__ = name of the function
print(__name__)  