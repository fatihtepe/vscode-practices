def multiply(a, b):
    print(a * b)

multiply(3 ,5)
multiply(-1, 2.5)
multiply('amazing ', 3) # it is amazing!

def motto():
    print('Be warrior not a worrier!')
motto()


def multiply2(a, b):
    return a * b 

print(multiply2(10, 5))


def my_function(a, b):
    print(a * b)

my_function(3, 4)



import datetime
# Function to print current date and time
def print_time():
    print('task completed')
    print(datetime.datetime.now())
    print()
    
first_name = 'Fatih'
print_time()

for x in range(0, 10):
    print(x)
print_time()




from datetime import datetime
# Function to print current date and time
def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()
    
first_name = 'Fatih'
print_time('printed first name')

for x in range(0, 10):
    print(x)
print_time('completed for loop')



# This function will return the first initial of a name
def get_initial(name):
    initial = name[0:1].upper()
    return initial

# Ask for someone name and return the initials
first_name = input('Enter your first name: ')
first_name_initial = get_initial(first_name)

last_name = input('Enter your last name: ')
last_name_initial = get_initial(last_name)

print('Your initials are: ' +first_name_initial + last_name_initial)



def my_function(a, b):
    hypotenuse = (a**2 + b**2)**0.5
    print(hypotenuse)
   
my_function(3, 4)



def my_function(a, b):
    hypotenuse = (a**2 + b**2)**0.5
    return hypotenuse

# print(my_function(3, 4))



def longer(a, b):
    if len(a) >= len(b):
        return a
    else:
        return b

print(longer('Richard', 'John'))




def my_function(a, b):
    area = (a * b)
    return area


def my_function(a, b):
    print(a * b)


    
for i in range(1, 51):
    if i % 5 == 0 and i % 3 == 0:
        print(f'{i}: FizzBuzz')
    elif i % 5 == 0:
        print(f'{i}: Buzz')
    elif i % 3 == 0:
        print(f'{i}: Fizz')
    else:
        print(f'{i}: zzzzzz...')


for i in range(1, 16):
    print('FizBuzz' if i % 15 == 0 else 'Fizz' 
        if i % 3 == 0 else 'Buzz' if i % 5 == 00 else i)
        



successful = True       
for number in range(1, 10, 2):
    print('Attemp', number, (number * '.'))       
    if successful:
        print('Successful')
        break
else:
    print('Attempted 3 times and failed')



for x in range(5):
    for y in range(3):
        print(f'{x}, {y}')



print(type(range(5)))

Iterable

for x in range(5):
    print(x)
    
    
for x in 'Python':
    print(x)
    

for x in [1, 2, 3, 4, 5]:
    print(x)

even = []
count= 0
for i in range(1, 10):
    if i % 2 == 0:
        even.append(i)
        count += 1
print(even)
print(f'we have {count} even numbers in the list {even}')
        
x = set(['p', 'q'])   
print(x)    



def greet_user(name):  
    print(f'Hi {name}') 

greet_user('Fatih')




def square(i):
    return i * i

print(square(2))
