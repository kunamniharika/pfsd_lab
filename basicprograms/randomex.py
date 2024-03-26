#---------------------------
'''


import random
n=random.randbytes(1)
print(n)

print(random.randrange(1,8))


print(random.randint(100,211))
mylist=("Samhitha","Rohitha","Divya","Jagruthi","Vishnu","Vasavi")
mylist1={"Samhitha","Rohitha","Divya","Jagruthi","Vishnu","Vasavi"}
mylist2=["Samhitha","Rohitha","Divya","Jagruthi","Vishnu","Vasavi"]
print(random.shuffle(mylist2))

'''

import string
import random
S=10
ran=''.join(random.sample(string.ascii_uppercase+string.digits,k=S))
s1=4
ran1=''.join(random.sample(string.digits,k=6))
print(ran1)