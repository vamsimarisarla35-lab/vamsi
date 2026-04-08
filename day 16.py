'''recursive function
----------------

def validate_pin(self):
    while self.remaining_attempts > 0:
        user_pin = input("enter 4 digit pin :")
        if len (user_pin) == 4 and user_pin == self.user_information:
            print("welcome to the ATM")
            return true
        else:
            self.remaing_attempts -= 1
            if self.remaining_attempts > 0:
                print(f"invalid pin. attempts left:{self}")
            else:
                print("card blocked.place contact coustmer care")
                return false

any = "python is a language"
vowel_list = []
con_list = []
def vowel_con(any,vowel_list,con_list):
    for j in any:
        if j in "AEIOUaeiou":
            vowel_list.append(j)
        else:
            con_list.append(j)
        print(f"{vowel_list} these are vowels")
vowel_con(any,vowel_list,con_list)



num = int(input("enter the number"))
def prime_cheek(num):
    if num <= 1 :        
        print("it is a prime")
        return
    for i in range(2,num):
        if num %i == 0:
            
           print(f"it is a not prime")
        return
    print(f"{num} is a prime number")
        
prime_cheek(num)'''
    

icici_ramayya_ac_details = {"Name":"Neduri jaichandra dasaradha ramayya",
                            "date-of-brith" : "15-06-2004",
                            "ATM PIN" : "113374",
                            "Balance" : 200000}
print("welcome to the icici bank")
print("please insert the ATM card")
icici_user_pin = input("please enter your 6 digits ATM pin : ")
if len(icici_user_pin) == 6:
    if icici_user_pin in icici_ramayya_ac_details['ATM PIN']:
        icici_user_choice = int(input("enter \n1.withdraw: \n2:deposite: ")) 
        if icici_user_choice == 1:
            money_w = int(input("enter the money to withdraw : "))
            if money_w <= icici_ramayya_ac_details['Balance']:
                icici_ramayya_ac_details['Balance'] -= money_w
                print(icici_ramayya_ac_details['Balance'])
            else:
                print("insuff")
        elif user_choice == 2:
            deposite_m = int(input("pls enter the money you want to deposite: "))
            if deposite_m % 100 == 0 and deposite_m >= 5000:
                icici_ramayya_ac_details['Balance'] += deposite_m
                print(f"you have deposite {deposite_m} and total is {icici_ramayya_ac_details['Balance']}")
            else :
                print(f"{deposite_m} you have entered is change or less than {5000}")
    else:
        print("the pin number is incorrect")
else:
    print("please enter the 6 digits numbers")





















































