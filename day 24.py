regular expression(reg ex)
----------------------------
-->this regular expression or regEx is a sequence of characters that forms a searching pattern.
--> to use this we have to import re,which will unlock the package

FUNCTONS
-----------
1.findall
-->by using this functon, it will find all sequence in the string
syntax-->re.findall(metacher,variable_name)
2.search
-------
-->by using this function ,it will only find first sequence in the string
syntax-->re.search ("metachar",variable_name)

metacharacters
---------------
-->metacharacters are used to form searching pattren
1.[]
----
--> in this meta character we can search for [a-z],[A-Z],[0-9]
2.dot(.)
------------
-->this meta character will  form a seaeching pttren as it will take any single character for (.)  
3.^
--------
-->this is used to find the string is starting with the sequence or number
SYNTAX -->re.finally("metachar",variable_name)
4.$
----------
this is used to find string is ending with the sequence or not
syntax-->re.findall("$",variable_name)
5.*
-----
-->this meta character will form a searching pattren as it well take any zero or more character for (*)
6.+
-------
-->this meta character will form a searching pattren as it will take a y one or more character for (+)
syntax -->re.search(".+",variable_name)



import re
any  = "this method ca9n read entair file and return into list with"
so =re.findall("[a-z]",any)
an = re.search("[a]",any)
print(so)


some = "by using this functon, it will find all sequence in the string"
an = re.search("[a]",some)
print(an)

import re
we = "hello"
the = re.findall("h...o",we)
thing = re.search("he..o",we)
print(the)
print(thing)

import re
sum = "welcome"
an = re.findall("w.....e",sum)
a = re.search("w.....e",sum)
print(an)
print(a)


import re
out = "this is used to find string is ending with the sequence or not"
one = re.findall("sequence $",out)
two = re.search("this $",out)
print(one)
print(two)



import re
vamsi = "this is used to find string is ending with the sequence or not"
gk = re.findall("c.*i",vamsi)
nk = re.search("t.*",vamsi)
print(gk)
print(nk)


import re
teja = "this meta character will form a searching pattren as it will take a y one or more character for (+)"
gk = re.findall("an.+y",teja)
koll = re.search("t.+",teja)
print(gk)
print(koll)




















































