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
obj.display()


2.MULTIPLE INHERITANCE
----------------------
--->



class father:
    def skill_1(self):
        print("father: hard working")
class mother:
    def skill_2(self):
        print("mother: cooking")
class child(father,mother):
    def skill_3(self):
        print("child: coding")
class brother:
    def skill_4(self):
        print("brother: dhola fellow")
any = child()
any.skill_1()
any.skill_2()
any.skill_3()
any.skill_4()

MULTI-LEVEL
-----------
--->THIS OCCURS WHEN A CLASS INHERITS FROM A CHILD CLASS, CREATING A GRANDPARENT--->CHILD IN THIS STRUCTURE.


class Grandparent:
    def show_Grandparent(self):
        print("I'm Grandparent")

class parent(Grandparent):
    def show_parent(self):
        print("I'm parent")

class child(parent):
    def show_child(self):
        print("I'm child")

any = child()
any.show_Grandparent()
any.show_parent()
any.show_child()


hierchical
---------------
--> this occurs when multiple child class inherit  from a single parent
class this process is called hierchical



class parent:
    def parent_(self):
        print("I am parent")
class child_1(parent):
    def child_(self):
        print("I am 1st  child")
class child_2(parent):
    def _child(self):
        print("I am 2nd  child")
class child_3(child_1,child_2):
    def child(self):
        print("I am the child")
thing = child_3()
thing.parent_()
thing.child_()
thing._child()
thing.child()'''


HYBRID INHERITANCE
------------------
---> Hybrid Inheritance is a type of inheritance that combines two or more types of inheritance
(like multilevel, multiple, or hierarchical) in a single program.  

class Parent:
    def parent_(self):
        print("I am Parent")

class Child1(Parent):
    def child1(self):
        print("I am Child 1")

class Child2(Parent):
    def child2(self):
        print("I am Child 2")

class Child3(Child1, Child2):
    def child3(self):
        print("I am Child 3")

obj = Child3()

obj.parent_()
obj.child1()
obj.child2()
obj.child3()














    





























































