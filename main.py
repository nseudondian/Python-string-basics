#String

intro = "Hello guys! welcome to Learn-In by N.S.E"

my_string = 'Hello World!'

print(intro, "\n", my_string)

multi_line = """Hey there!
I am on multiple lines"""

multi_line = '''Hey there!
I am on multiple lines'''

age = "18"
print(type(age))

x = 18
print(type(x))



#String operations

#concatenation - put two or more strings together using the addition (+) operator

first = "Hello"
second = "World!"
third = "beautiful people"
result = first + " " + second + " " + third
print(result)

print("hello" + " " + "world")


x = '4'
y = '5'
n = '0'
z = x + " " + y + " " + n

print(z)

#String Replication - Multiplying a string with a number

# msg = "Hello"
# print (msg * 100)
#Accessing characters - accessing each character of a string using indexing

msg = "Hello"

print("character at index 0:", msg[0])
print("character at index 1:", msg[1])
print("character at index 2:", msg[2])
print("character at index 3:", msg[3])
print("character at index 4:", msg[4])

message ="Hello World!"
print(message[-6])
print(message[-1])

print('NSE'[-1])
#slicing - extracting a substring from a string
#syntax: string[start:end:step]

msg = "Hello World!"

new_msg = msg[0:5:1] 

new_msg = msg[0:5:2] 

new_msg = msg[0:5] 

new_msg = msg[:5] 
new_msg = msg[::2] 

new_msg = msg[2:] 


print(new_msg)

age = input("how old are you? ")

print(age)

print("I am "  + age +   " years old")
