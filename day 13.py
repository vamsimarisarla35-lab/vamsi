num = int(input("enter the numbere : "))
for j in range(num):
    for i in range(j):
        print("153",end = "")
    print()



num = int(input("enter the numbere : "))
for j in range(num):
    for i in range(j):
        print("*",end = "")
    print()
   



num = int(input("enter the numbere : "))
for j in range(num):
    for i in range(num):
        print("*",end = "")
    print()
   

num = int(input("enter the numbere : "))
for j in range(num):
    for i in range(num-j):
        print("*",end = "")
    print()



num = int(input("enter the numbere : "))
for j in range(num):
        print(" " *(num -j) ,end = "")
        for i in range(j+1):
            print("*",end=" ")
        print()''' 


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
        
        










































    








