count = 0
print('Starting')
while count < 10 :
    print(count, ' ', end='')  # starts from 0
    count += 1
print()
print('Done')


count = 0
print('Starting')
while count < 10 :
    count += 1
    print(count, ' ', end='')  # starts from 1
print()
print('Done')


print('Print out values in a range')
for i in range(0, 10):
    print(i, ' ', end='')
print()
print('Done')


for _ in range(0, 10):
    print('.', end='')
print()


print('Only print code if all iterations completed')
num = int(input('Enter a number to check for: '))
for i in range(0, 6):
    if i == num:
        break
    print(i, ' ', end='')
print('Done')



for i in range(0, 10):
    print(i, '', end='')
    if i % 2 == 1:
        continue
    print('hey its an even number')
print('Done')    


import random

MIN = 1
MAX = 6

roll_again = 'y'

while roll_again == 'y':
    print('Rolling the dices...')
    print('The values are....')
    dice1 = random.randint(MIN, MAX)
    print(dice1)
    dice2 = random.randint(MIN, MAX)
    print(dice2)
    roll_again = input('Roll the dices again? (y / n): ')


practice_again = 'y'

while practice_again == 'y':
    print('This is while loop baby!')
    practice_again = input('Do you wanna continue? (y / n): ')
if practice_again == 'n':
    print('End of lesson')



words = ['cat', 'window', 'door', 'dog']
for w in words:
    print(f'In the list the length of the word {w} is {len(w)}.')

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, ':', a[i])


number = input('Please input the number:')

if number.isnumeric():
    num = int(number)

    if num == 0:
        # Termination criteria
        print('0! factorial is 1')
    else:
        # Recursive element
        factorial = 1
        for i in range(1, num + 1):
            factorial = factorial * i
        print(number + '! factorial is', str(factorial))

else:
    print('Not an integer number')




# Determine if a number is a prime number
number = input('Please input the number:')
if number.isnumeric():

    num = int(number)

    if num <= 2:
        print('Number must be greater than 2')
    else:
        # Assume a number is a prime number until proved otherwise
        prime_number = True
        for i in range(2, num):
            for j in range(2, i):
                # If there is no remainder then its not a prime number
                if i % j == 0:
                    prime_number = False
                    break
            if prime_number:
                print('Prime number', i)
            prime_number = True
else:
    print('Must be a positive integer')


a = 3
print('A is positive number') if a > 0 else print('A is negative')

num = int(input('please enter a number: '))
if num > 0 and num % 2 == 0:
    print(f'{num} is positive and even number')
elif num > 0 and num % 2 != 0:
    print(f'{num} is a positive number and odd number')
elif num == 0:
    print(f'{num} is zero')
else:
    print(num,'is negative')


sayi = -15

# print('sayi pozitifdir') if sayi > 0 else print('sayi negatiftir.')

if sayi > 0:
    print('positive')
elif sayi < 0:
    print('negative')
else:
    print('zero')

user_name = input('Enter your name: ')
access_level = int(input('Enter access level: '))

if user_name == 'admin' and access_level >= 4:
    print('Access granted!')
else:
    print('Access denied!')


user_name = input('Enter your name: ')
access_level = int(input('Enter access level: '))

if user_name == 'admin':  
    print('Access granted!')
elif access_level >= 4:
    print('Access granted!')
else:
    print('Access denied!')



while  True:
    games = input("istediğiniz oyun: ")
    if games == ("cs"):
            version = int(input("Hangi sürüm olacak: "))
            if (version == 1 or version == 2):
                print("ücret 30 TL")
                continue
            elif (version == 3):
                print("ücret 40 tl")
                continue
            else:
                print("aradığınız version  yoktur")
    elif games == ("mod"):
            version = int(input("Hangi sürüm olacak: "))
            if (version == 1 or version == 2):
                print("ücret 30 TL")
                continue
            elif (version == 3):
                print("ücret 40 tl")
                continue
            else:
                print("aradığınız version  yoktur")
    elif games == ("ets"):
            version = int(input("Hangi sürüm olacak: "))
            if (version == 1 or version == 2):
                print("ücret 30 TL")
                continue
            elif (version == 3):
                print("ücret 40 tl")
                continue
            else:
                print("aradığınız version  yoktur")
    else:
        print("istediğiniz oyun yoktur")
        continue




count = 0
while count < 5:
    print(count)
    count +=1
else:
    print(count)


count = 0 
while count < 5:
    print(count)
    count += 1
    if count == 3:
        break



language = 'Python'
for letter in language:
    print(letter)


person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

for key in person:
    print(key)

for key, value in person.items():
    if key == 'country':
        continue
    print(key, value) 
    

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)


for i in range(11):
    print(i)

i = 0
while i < 11:
    print(i)
    i += 1
  
  
for i in range(10, -1, -1 ):
    print(i)

for i in range(8):
    print(i * '#')

for i in range(8):
    print('# ' * 8) 

    
for number in range(3):
    print('Attempt', number + 1, (number + 1) * '.')

successful = False
for number in range(3):
    print('Attempt')
    if successful:     
        print('Successful')
        break
else:
    print('Attempted 3 times and failed')
    
for x in range(5):
    for y in range(3):
        print(f'({x}, {y})')



names = ['Ahamed', 'Annah', 'James', 'Jamila']
for name in names:
    print(name)



person = {
    'name': 'Fatih',
    'age': 45,
    'addres': 'Canada'
}

for key, value in person.items():
    print(f'{key}:{value}')

for key in person:
    print(f'key:{key} value:{person[key]}')


result = 0
numbers = [1, 3, 5 ,6, 7, 8, 9]
for number in numbers: 
    result += number
    
print(f'Result = {result}' )


number = 0

while number < 10:
    print(number)
    number += 1
else:
    print('while loop ended')



number = 0

while number < 10:
    if number == 5:
        break
    number += 1
    print(number)


number = 0

while number < 10:
    number += 1
    if number < 5:
        continue
    print(number)
    
    

for n in [1, 2, 3, 4, 5, 6, 7, 8]:
    if n < 5:
        continue
    print(n)
    
    
    
for n in [1, 2, 3, 4, 5, 6, 7, 8]:
    if n == 5:
        break
    print(n)


name = 'fatih'
email = f'''
hello {name},
how are you?
it was nice talking to you
age {4+4}
'''
print(email)





