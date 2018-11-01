#--------------------- Classes -  getter setter
class Person:
    def setFullName(self,firstName,lastName):
        self.firstName=firstName
        self.lastName=lastName
    def printFullName(self):
        print(self.firstName, " ",self.lastName)

personName=Person() # instance of class
personName.setFullName("Zeeshan","Talib")
personName.printFullName()