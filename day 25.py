'''
7.?
-----
--> this meta character will form a searching pattren as it will take any zero ore one character for (?)
syntax--> re.findall(" .?",variable_name)

8.{}
------
-->this meta character will form a searching pattren as we can menction the size in the {}
syntax-->re.search(".{size},variable")

9.|
----
-->this meta character will form a searching pattren as it consider right or left any string is present or not for (|)

10. specal sequencey is a \followed by one of the character in hte list below ,and has a

special meaning

\A
----
returns a match if the spacefied character are at the begining of the string
eg: "\ATHE"

\b- return a match where the specified character are at the begining or at the end of a word
eg: r"\bain"

\s- return a match where the string contains a white space
character
eg: "\s"



import re
any = "this is meta character"
an = re.findall(" th.?",any)
print(an)




import re
any = "this meta character will form a searching pattren as we can menction the size in the "
an = re.findall(" .{25}",any)
print(an)


import re
any = "this meta character will form a searching pattren  "
an = re.findall(" that|this",any)
print(an)



import re
txt = "The rain in spain"
#check if the string starts with "The":
x = re.findall("\AThe", txt)
print(x)
if x:
    print("Yes, there is a match!")
else:
    print("No, match")



import re
txt = "The rain in Spain"
#check if the string starts with "The":
x = re.findall("r\bSpain", txt)
print(x)
if x:
    print("Yes, there is a match!")
else:
    print("No, match")



import re
txt = "The rain in Spain"
#check if the string starts with "The":
x = re.findall("\s", txt)
print(x)
if x:
    print("Yes, there is a match!")
else:
    print("No, match")



time and date
-----------------
%D------>day
%M------>month
%Y------>year
%H------>hour
%M------>min
%S------>sec
%P------>AM/PM
%A------>day name
%B------>month name

'''

import datetime
now = datetime.datetime.now()

print(today.strftime("%d-%m-%Y"))
print(today.strftime("%A"))
print(today.strftime("%B"))


















































