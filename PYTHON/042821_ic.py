number_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result= list(filter(lambda x:x%2==1, number_list))   
print(result)


grocery = "bread", "water", "oil"
enum_grocery = list(enumerate(grocery,1000))
print(enum_grocery)


numbers = [2.5, 30, 4, -15]
numbers_sum = sum(numbers)
print(numbers_sum)
numbers_sum = sum(numbers, numbers_sum)
print(numbers_sum)


print(round(3.675, 2))


def multiply(a, b) :
    print(a * b)
    
multiply(3, 5)
multiply(-1, 2.5)
multiply('amazing ', 3)

def add (a, b):
    print( a + b)
    
add (5 ,5)

    

def calculator (a, b, c):
    if c == "+":
        print(a + b)
    elif c == "-":
        print(a - b) 
    elif c == "*":
        print(a * b) 
    elif c == "/":
        print(a / b) 
    else:
        print('enter valid operator')
        
calculator(8, 8, '*')


def listem():
    return [1, 2, 3, 4, 5]

print(listem())


def calculator(a, b, c):
    if c == "+":
        return (a + b)
    elif c == "-":
        return (a - b)
    elif c == "/":
        return (a / b)
    elif c == "*":
        return (a * b)
    else:
        print("please enter right parameter!..")
print(calculator (2, 7, "/"))



number = int(input("Please enter a number : "))
for i in range(2, number):
    if number % i == 0:
        print(number,"is not a prime number")
        break
else:
    print(number,"is a prime number")




# To find prime number
n = int(input('Enter a number to check if it is a prime number: '))
count = 0

for i in range(1, n+1):
    if not n % i:
        count += 1
if (n == 0) or (n == 1) or (count >= 3):
    print(n, 'is not a prime number')
else:
    print(n, 'is a prime number')
    
    
n = int(input("Enter a number to check if it is a prime number."))
count = 0
for i in range(1, n+1) :
    if n % i == 0 :
        count += 1
if (n == 0) or (n == 1) or (count >=3) :
    print(n, "is not a prime number.")
else:
    print(n, "is a prime number")