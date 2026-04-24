'''polymorphism
--------------
---> this allows a object of different classes to be treated as instance of the same base class, with methods behaving differently based on the actual abject type.
print(len("python"))
print(len([1,2,3,4]))

merhod overloading
---------------------
--> this defines multiple methods with the seme name but different parameters (number,type,or order)in the same class




class calculator:
    def add(self ,a,b = 0,c = 0):
        return a+b+c
cal = calculator()
print(cal.add(2))
print(cal.add(3,4))
print(cal.add(5,7,8))



class calculator:
    def sub(self ,a,b = 2,c = 1):
        return a-b-c
cal = calculator()
print(cal.sub(5))
print(cal.sub(11,4))
print(cal.sub(12,5,20)

mehod overloadsing
-->this occurs in the child class ,redefining a parent class method with  the same signature for runtime.



class animal:
    def speak(self):
        return"sound"
class dog(animal):
    def speak(self):
        return "wolf"
dog = dog()
print(dog.speak())



class animal:
    def speak(self):
        return"sound"
class snake(animal):
    def speak(self):
        return"shuu"
snake = snake()
print(snake.speak())


class music:
    def music(self):
        return"sound"
class visual(music):
    def music(self):
        return"pepepe"
music = music()
print(visual.music())
    

operator overloading
-------------------------
----> this is cusomizes operator like +,- for user-define classes by implementing special method ....
eg... _add,sub_'''

class someone:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        return someone (self.a +other.a,self.b + other.b)
    def __str__(self):
        return f"((self.a),(self.b))"
any = someone(2,3)
so = someone(5,9)
print(any + so)































































