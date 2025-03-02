import sys
from sys import platform

class Person:
    def hi():
        print(sys.platform)
        print("HELLO!")
        print(platform)
        

p = Person
p.hi()