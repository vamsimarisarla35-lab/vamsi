'''functions()
-----------------
-->this is a block of code with is reusable.
-->two types 1.built-in or in-buid
             2.user define


1.built-in or in-build
---------------------------------
-->they comes with program and those are already defined......
eg..

2.user define
-------------
-->this created by person who developing or using for developing

note
-----
-->ir's start with def keyword followed by func name
-->and it has calling function 

def functin name(a,b):   #function is defined where a,b are perameters
    ------------------------
    -------------------------
    ------------------------
fun_name(argument) #calling fune


a = 5
def even_odd (a):
    if a % 2==0:

        print(" 2 ia a even")
    else:
        print("not even")

even_odd(a)'''


#prime numbres in functions
a = int(input("enter the number"))
count = 0
def prime_cheek(a,k):
    for j in range (1,a+1):
        if a%j == 0:
            k+=1
    if k == 2:
        print("prime number")
    else:
        print("not prime number")
prime_cheek(a ,count)
    
            

































































             
