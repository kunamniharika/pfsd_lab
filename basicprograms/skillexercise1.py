#---------------------------
'''
n=int(input("Enter a Number"))
if n==0:
    print("Wrong Input")
else:
    for i in range(n,n+1):
        val=n*(n*1)
        print(val)
'''



#---------------------------
'''
x=0
str1="thisismycountryindia"
for i in str1:
    x=x+1
    print(str1[0:x])
for i in str1:
    x=x-1
    print(str1[0:x])
'''


#---------------------------
'''
n=int(input("Enter a Number"))
for i in range(0,n):
    for j in range(0,i+1):
        print("* ",end="")
    print("\r")
for i in range(n,0,-1):
    for j in range(0,i):
        print("* ",end="")
    print("\r")
'''


#---------------------------
'''
a1=1234
a3="10100"
a2=int(format(int(a3,2),'d'))
print(a2)

a4=1045
a5=format(a4,'x')
print(a5)
'''


#---------------------------
'''
numbers = [1, 2, 3, 4, 5]
average = sum(numbers) / len(numbers)
print(f"The average is: {average}")
'''

#---------------------------
'''


user_input = input("Enter an integer value: ")
converted_value = int(user_input)
print("Converted integer value:", converted_value)

'''


#---------------------------
'''
def is_right_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()
    if sides[2] ** 2 == (sides[0] ** 2) + (sides[1] ** 2):
        return True
    else:
        return False
a = float(input("Enter the length of side A: "))
b = float(input("Enter the length of side B: "))
c = float(input("Enter the length of side C: "))

if is_right_triangle(a, b, c):
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")

'''





