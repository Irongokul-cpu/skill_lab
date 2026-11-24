'''
import keyword
print (keyword.kwlist)


a=None
print(a)
a=0
print(type(a))
print(bool(a))
print(bool(0.0))
print(bool(1.8))
print(int())

a=3j+5
print(a)

a="Happy Father's Day"
print(a)
# To access F 
print(a[6])

#list
my_list = [1, 2, 3, 4, 'hello', 5.6, True]
# to Extract hello from the list
print(my_list[4])
# Now H from hello 
print(my_list[4][0])

#Appened Function
my_list.append(10)
print(my_list)

#Pop Function
print(my_list.pop())
print(my_list)

#Tuple
my_tuple = (1, 2, 3, 4, 'hello', 5.6, True)
print(type(my_tuple))

#SET
my_set = {1, 2, 3, 4, 'hello', 5.6, True}
print(type(my_set))
print(my_set)


#Dictionary
my_dict = {'a': 1, 'b':[10,20,30], 'c': 3}
print(type(my_dict))
print(my_dict)

#Adding new key-value pair
my_dict['d'] = 4
print(my_dict)

#Accesing 20 from the list in the dictionary
print(my_dict['b'][1])'''


'''Slicing
a="Hello World"
print(a[0:5])
print(a[6:11])
print(a[2:4])
print(a[2:3+1:3])

#Accesing from right to left 
print(a[-8:-10:-1])

a="Good Morning"
print(a[7:11])

#Same with negative indexing 
print(a[-5:-1])


a="Hello"
print(a[-2:-5:-1])
print(a[::-1]) #Reverse the string
a="Good Morning"

# extract odM
print(a[1:5+1:2])

#extract Mng
print(a[5::3])

print(a[-7::3])

print(a[-2:-8:-3])

#collection type input 
a=eval(input("Enter a: "))
print(a,type(a))'''




'''a=int(input("Enter a: "))
if(a%2==0):
    print("Even")
else:
    print("Odd")'''

'''#Check wheteher the length of list is 5 or not 
a=eval(input("Enter a list: "))
if(len(a)==5):
    print("The length of the list is 5")
else:
    print("The length of the list is not 5")'''
'''print(ord('j')+ord('a')+ord('v')+ord('a'))
print(chr(65))
print(chr(97))

#how to covert capital letter to small letter and vice versa without using inbuilt function
ch=input("Enter:")
if "A"<=ch<="Z":
    print("Upper case letter")
elif "a"<=ch<="z":
    print("Lower case letter")
else :
    print("Not a letter")'''
'''#Username and password validation
un=input("Enter username:")
if un=="admin":
    pwd=input("Enter password:")
    if pwd=="admin123":
        print("Login successful")
    else:
        print("Invalid password")'''
'''i=1
while (i<=50):
    if i%2==0:
        print(i)
    i+=1


n=int(input("Enter a number: "))
rev=0
while(n>0):
    ld=n%10
    n=n//10
    rev=rev*10+ld
print( rev)'''



'''l={10,20,30}
for i in l:
    print(i)

ch=input("Enter:")
for ch in ch:
    if "A"<=ch<="Z":
        print(chr(ord(ch)+32))
    elif "a"<=ch<="z":
        print(chr(ord(ch)-32))
    else:
        print("Not a letter")


s=input("Enter a string: ")
rev=""
for i in s:
    rev=i+rev
print(rev)'''


'''#Nested for Loops 
for i in range(1, 6):
    for j in range(1, 6):
        print('*', end=' ')
    print()'''



for i in range(1, 6):
    for j in range(1, 6):
        if i==j:
            print('*', end=' ')
        else:
            print('@', end=' ')
    print()

#Triangle Pattern
for i in range(1, 6):
    for j in range(1, 6):
        if j<=i:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()