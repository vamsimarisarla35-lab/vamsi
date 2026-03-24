'''
string ---> string is a collaction of char ,with represter by "" or ""and we can acess the using indexing and  also slicing  '''

any = 'python programming'
print (any[7])

#slicing and also indexing

any = 'python programming'
print(any[7:13])

#this also immutable ,where i could not able to modification on thet perticular value
any = 'python proigramming'
so = any.replace ("python","java")
print(any)
print(so)

any = 'python programming'
print(any[-6])

a_day = ("i'm vamsi from rajam, have 3+years exp as ")
print(f"my name is {a_day[4:9]}")
print(f"i'm vamsi from{a_day[13:18]}")

#reverse
day = 'teja'
print(day[::-1])

#integer convrt the strings, if the contain only integers valus ....
some = "123"
num = int(some)
print(type(num))

#note [methods of string
#------------
#split()--->remove space, and  the is in the list[] it will give separated thing in each ind

#syntax--->variable_name.split("substring")
#lower()--->this is used to convert all letters into  lower case

some = "python is a programming language"
print (some.split(" "))


some = "python is a programming language"
print (some.split("programming "))


some = "python is a programming language"
print(some.lower())


some = "python is a programming language"
print(some.upper())


#replace  method

some = "python is a programming language"
print (some.replace("programming ","high level"))


some = "python is a programming language"
if "pythn" in some:
    print("yes")
else:
    print("no")













































