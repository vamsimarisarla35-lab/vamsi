'''print(8+8)
print("python" + "language")
print([1,2] + [3,4])

concatenation
----------
this is nothing but, a (+) behavi..
case_1
-----
intergers---this will act as addition for the int

case2
------
for other  data types (we have to use same type)this (+) act as concatenation
note:can only concatenate str (not "list" to str)

tuple()--->
is a collection of different datatype and this is  represente by (), separated by (,)
eg...

thing = (1,"vamsi",[1,2],(8,9))'''

thing = (12,89,"python",(23,"vamsi",[67,"pthon is a language",(7,8)],[8,("python",[34,9])]))
print(thing)


num_1 = 9
num_2 = 90
print(f"before swapping num_1 = {num_1} and num_2 = {num_2}")
num_1,num_2 = num_2,num_1
print(f"after swapping num_1 = {num_1} and num_2 = {num_2}")


leap_year = int(input("enter year"))
if (leap_year% 4 == 0 and leap_year % 100 != 0)or leap_year % 400 == 0:
    print(f"yes,{leap_year} is a leap year")
else:
    print(f"no,{leap_year} is a leap year")











































