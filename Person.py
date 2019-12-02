## This class is used to create a Person object so that each person can have a phone number as well as a name. Pretty simple. 
class Person:
    
    def __init__(self, name, number): ## Constructor
        self.name = name
        self.number = number

    def getName(self): ## Get the name
        return self.name
    
    def getNumber(self): ## Get the number
        return self.number

    def setName(self, name): ## Set the object's name
        self.name = name
    
    def setNumber(self, number): ## Set the object's number
        self.number = number
    
    def printPerson(self):
        print(self.name + ":" + self.number)