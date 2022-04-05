num1 = 42 #variable declaration
num2 = 2.3 #variable declaration
boolean = True #Data Types primitive
string = 'Hello World' #Data Types primitive
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}#list
fruit = ('blueberry', 'strawberry', 'banana')#list
print(type(fruit))#function
print(pizza_toppings[1])#function
pizza_toppings.append('Mushrooms')#variable declaration
print(person['name'])#function
person['name'] = 'George'#variable declaration
person['eye_color'] = 'blue'#variable declaration
print(fruit[2])#function

if num1 > 45:#conditional
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:#conditional
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): #for loop
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5): #while loop
    print(x)
    x += 1

pizza_toppings.pop()#function
pizza_toppings.pop(1)#function

print(person)#function
person.pop('eye_color')#delete value
print(person)#function

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni':#conditional
        continue
    print('After 1st if statement')#function
    if topping == 'Olives':#conditional
        break

def print_hello_ten_times():#function
    for num in range(10):#for loop
        print('Hello')#function

print_hello_ten_times()#function

def print_hello_x_times(x):
    for num in range(x):#for loop
        print('Hello')#function

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):#for loop
        print('Hello')#function

print_hello_x_or_ten_times()#function
print_hello_x_or_ten_times(4)#function


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)