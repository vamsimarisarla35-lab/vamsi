'''#ENCAPSULATION
-------------
--->THE PRINCIPLE OF BUNDING DATA(ATTRIBUTES) AND METHODS THAT OPERATE ON THAT DATA INTO A SINGLE UNIT, WHICH IS CLASS.


class bankAC:
    def _init_(self,balance):
        self.__balance

    def deposite(self,amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
Acc = bankAC (15000)
Acc.deposite (7000)
print(Acc.get_balance)

inheratance
------------
-->this allows a child (subclass) to acquire the attributes and methods of a parent class ) this is called inheratance
1.single inheritance
2.multiple


-->using single method of the class from base class is know as single 

super()
-------
-->this is used to call methods of yhe parent class from the child class 


class parent:
    def display(self):
        print("this is a parent method")
class child (parent):
    def display(self):
        super().display()
        print("this is child method")
obj = child()
obj.display()'''



class fatheer:
    def skill_1(self):
        print("father:hard working")
class mother:
    











































