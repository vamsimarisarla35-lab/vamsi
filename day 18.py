'''#generators
--------------
--> This is a special type of function that return a iterator which one at a time
--> 'yield' ==>it will take a pass and again resume,this is not a nrml keywoord cant be used in the nrml functions

def my_generator():
    yield 1
    yield 2
    yield 3

an = my_generator()

print(next(an))
print(next(an))
print(next(an))
--> it will take a pause and again resume, this also not a nrml keyward can not be used in the normal function
---> this is used to produce a value and pause executon

next()
-----------
--> this is used  to get next value from a generator
--> when the value is finished ,it will stop the iterator'''


'''
def square_gen(n):
    for i in range(n):
        yield i

for j in square_gen(50):
    print(j)




for i in range(0,101):
    if i % 2 == 0:
        print(f"{i} is even num")
    else:
        print(f"{i} is odd num")'''




def check_even_odd():
    for i in range(n +1):
        if i % 2 == 0:
            print(f"{i} is an even number")
        else:
            print(f"{i} is an odd number")
print check_even_odd()








    
