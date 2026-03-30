'''any_ = "pythomn is a programming language"
vowle_cou = 0
space_cou = 0
con_cou = 0
for j in any_:
    if j in "AEIOUaeiou":
        vowle_cou += 1
    elif j == " ":
        space_cou += 1
    else:
            con_cou += 1
print(vowle_cou)
print(space_cou)
print(con_cou)


any_ = "pythomn is a programming language"
vowle_cou = 0
space_cou = 0
con_cou = 0
for j in any_:
    if j in "AEIOUaeiou":
        vowle_cou += 1
    elif j == " ":
        space_cou += 1
print(f"this is count of all vowle in the string {vowle_cou}")
print(f"this is count of all space in the string {space_cou}")
print(f"this is count of all cons_ in the string {len(any_)-(vowle_cou + space_cou)}")


a = 9
print(a)
for j in range (1,10):
 print(j)
 
#range---> this is used to generate number
#syntex--->range (start,end,step)
for j in range(1,10,3):
     print(j)


any = "123"
print(int(any))
print(list(any))
print(tuple(any))


so = "123"
print(str(so))
print(float(123))

an = [1,2,3]
vs = str(an)
print(type(vs))
print(vs)
print(tuple(an))


a = [(1,2),(3,4)]
print(dict(a))

rev_str = "vamsi"
empty_ = ""
for j in rev_str:
    empty_ = j + empty_
    print(empty_)


rev_str = "vamsi"
empty_ = ""
for j in rev_str:
    empty_ = j + empty_
    print(empty_ )
if empty_ == rev_str:
    print(f"{rev_str} is palin")
else:
    print(f"{rev_str} is  not a palin")


rev_str = "madam"
empty_ = ""
for j in rev_str:
    empty_ = j + empty_
    print(empty_ )
if empty_ == rev_str:
    print(f"{rev_str} is palin")
else:
    print(f"{rev_str} is  not a palin")'''

for num in range(1,100):
    if num % 2 == 0:
        print(f"{num} is a even num")
    else:
        print(f"{num} is a odd num")
        


















    
    








































     




















