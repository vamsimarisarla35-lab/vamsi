'''for j in range(2,100):
 print(j)

prime_num = int(input("enter the number:"))
count = 0
for j in range(1,prime_num+1):
    print(j)
    if prime_num % j == 0:
        count += 1
        print(count)
if count == 2:
    print(f"{prime_num} is a prime number")
else:
    print(f"{prime_num} is not a prime number")


for an in range(2,100):
    count = 0
    for j in range (1,an+1):
        if an % j == 0:
            count += 1
    if count == 3:
        print(f"{an} is a prime")
    else:
        print(f"{an} is a not prime")


list_1 =[12,14,2,3,65]
for j in list_1:
    count = 0
    for n in range (1,j+1):
        if j % n  == 0:
           count += 1
    if count == 2:
        print(f"{j} is a prime")
    else :
        print(f"{j} is not a prime")'''


any = [2,3,4,2,5,8,7,8,9,8,7]
empty_ = []
for j in any:
    if j not in empty_:
        empty_.append(j)
        print(empty_)
    else:
        any.remove(j)
        print(any)



















        
        



        
