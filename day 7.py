vowles_con = input("enter a lettert")
  if vowles_con in "AEIOUaeiou":
      print("vow")

else:
    print("con")

time_aday = input("enter 24 hours time :")
parts = time_aday.split(":")
hours_ = int(parts[0])
min_ = int(parts[1])
if  hours_ >=13 and min_ <60:
    print(f"{time_aday}convert into {hours_ -12}:{min_}pm")

else:
    print(f"you have entered nrml or min are incorrect")

#list--->different types inside the [],which are separated by

list_1 = [1,2,3,"python",[1,2,["python","java"],"language"]]
print(list_1[4][2][0][3])
    
list_ = [1,2,3,4,"vamsi",[4,5,6,"data"],["atchuth","pavan"]]
print(list_[6][0][6])

#methods of list
#append()--->this method is used to add new items into lidt it will only go to the last index of the list 
#extend()--->this method is used to add item to list in the last index, where each item or substract is in the list
#remove()--->this method will delete the item or value directly
#pop()
#mutable--->i can directly modify on that particular variable
#immutable--->i can not modify directly on that particular variable


list_2 = [1,2,3,4,5]
list_2.append(555)
print(list_2)


list_2 = [1,2,3,4,5]
list_2.extend(["vamsi",2,3,4])
print(list_2)


list_3 = [1,2,3,4,5]
list_0 = list_3.extend(["vamsi"])
print(list_0)

list_4 = [1,2,3,["python"]]
list_4.remove(2)
print(list_4)


list_4 = [1,2,3,["python"]]
list_4.pop(2)
print(list_4)


list_4 = [1,2,3,["python"],["letter"]]
list_4.pop("letter")
print(list_4)
 



















