'''constructor(__init__)
----------------------
-->a constructor is a special method used to installize object data
__init__()

class student:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def display(self):
        print(self.name,self.id)
stu_1 = student("teja",123)
stu_1.display()

access specifiers
----------------------
1. public
syntax --name
we can use it any where in the program

2. protected
the syntax is _name
this is only for internal use

3.private
syntax __name
this one is restricted

self
----
-->this keyward is instance variable and unique for each  object





class some:
    def__init__(self)
    self.public = "public"
    self.protected = "proctected"
    self.private = "private"

any = some()
print(any.__public)
print(any.proctected)
print(any.private)

'''

icic_teja_ac_details = {"name" : "teja","atm pin" : "6688", "blance" : 5000}
icic_user_pin = input("pls enter your 4 digit atm pin: ")
if len (icic_user_pin) ==4:
    if icic_user_pin in icic_teja_ac_details['atm pin']:
        user_choice = int(input("enter \n1.withdraw:"))
        if user_choice == 1:
            money_w = int(input("enter money want to withdraw"))
        if money_withdraw <=icic_teja_['blance']:
            icic_teja_['blance'] -=money_w
            print(icic_teja_['balance'])
        else:
                print("insuff")
        
        















































