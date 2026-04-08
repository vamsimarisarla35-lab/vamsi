#erquired origiments
#--------------------


num = 9
num_2 =10
def add (num,num_2):
    print(num +num_2)
add(num,num_2)



#----->  it should nit match same number variable in calling with def
#dafult argument
#-----------
#--> it will take the defult values from the arguments
my_name = "vamsi"
def add (my_name):
    print(my_name)
add("marisarla")
# arguments can be passed in calling ,they work


def prime_cheek(num ,count ):
    for j in range(1,num+1):
        if num % j == 0:
            count += 1
    if count == 2:
            print("it is a prime number")
    else:
        print("it is not a prime number")
prime_cheek(num = 45,count=0)
prime_cheek(num = 7,count=0)
# passing values to variables using '=' in the calling function

def any(num ,num_2,num_3):
    print(f"num ={num},num_2 {num_2},num_3{"vamsi"}")
any(num_2=7,num=0,num_3 = "vamsi")


def name(*candidate):
    print(candidate)
name(10,20,30)


#syntax earror

#1) if a functoin parantheis is not colosed properly it will result in  STNTAX EARROR
#2)startment should end with a proper column
#30 indatation earror
#4)attribute earror
#5)type earror 















































    
