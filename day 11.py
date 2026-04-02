'''table_num = int(input("enter the number"))
for j in range(1,11):
    print(f"{table_num} x {j} = {table_num * j}")'''

#string methods
#-----------------
#count(),join(),strip(),replace(),split(),casefold(),isalnuml(),isalpha(), isdigit(),
#capitalize(), isdecimal(), islower(),isupper()


an = "Python is a Programming Language"
count_U = 0
count_L = 0
for ch in an:
    if ch.isupper():
        count_U += 1
    elif ch.islower():
        count_L += 1
print(f"there are total {count_U} cap L")
print(f"there are total {count_L} small L")



an = "Python is a Programming Language"
cap_L = []
small_L = []
for ch in an:
    if ch.isupper():
        cap_L.append(ch)
    elif ch.islower():
        small_L.append(ch)
print(f"{cap_L} cotain all cap L")
print(f"{small_L} cotain all small_L")


icic_teja_ac_details = {"name" : "teja","atm pin" : "6688"}
print("welcome to icic atm")
print("pls enter yout atm card")
icic_user_pin = input("pls enter your 4 digit atm pin: ")
if len (icic_user_pin) ==4:
    if icic_user_pin in icic_teja_ac_details['atm pin']:
        print("the pin is correct")
    else:
        print("you have entered invalid pin")
else:
    print("pls enter 4 digit pin")



per_num = int(input("enter a number"))
fact_all = 0
for j in range(1,per_num):
    if per_num % j ==0:
        fact_all += j
if fact_all == per_num:
    print(f"{per_num} is the perfect num")
else:
    print(f"{per_num} is not perfect num")


































































