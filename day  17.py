lamda functions ()
-----------------------
--> this is also called anonymous function
-->a lamda function can take n numbers of arguments but have only one expression

synatax
-----------
lamda (keyword) arguments : expression


any = lambda so : so + 10
print(any(6))

some = lambda an,how,do :(how - an)*do
print(some(4,9,2))


list comprehension:
---------------------
--> this is offers the shorter syntax when you want to create a new list
from the existion list
     
syntax
--------
            variable_name = [expression loop and condition]


old_list = [1,2,3,4,5,6,7,8,9,4,5,4,4,6,4,1,4,2]
new_list = [j for j in old_list if j%2== 0]
print(new_list)























