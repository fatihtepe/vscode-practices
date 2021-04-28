numbers = [12, 37, 5, 42, 8, 3]
even = []
odd = []
while len(numbers) > 0:
    number = numbers.pop()
    if(number % 2 == 0):
       even.append(number)
    else:
       odd.append(number)
print(even)
print(odd)
               
               
people = ['John', 'Anne']

for name in people:
   print(name)
   
# let's do it with while loop

index = 0
while index < len(people):
      print(people[index])
      index = index + 1
      
my_list = ['a', 'b', 'c', 'd', 'e']
a = 0
while a < len(my_list):
   print('the square of {} is equal to: {}'.format(a, a ** 2))
   a += 1


my_list = ['ahmet', 'basak', 'cenk', 'deniz', 'emre']
index = 0
while index < len(my_list):
   print(my_list[index])
   index = index + 1



fruites = ['apple', 'orange', 'banana', 'grape', 'strawbery']
i = 0
while i < len(fruites):
   print(fruites[i])
   i = i + 1
   

a = 1

while a < 10:
   print('Nicely done!')
   a += 1


age = input('Please enter your age: ')
while not age.isdigit():
   print('it is invalid format!')
   age = input('Please try again!: ')
print('Greate! You entered a valid age format')



age = input('Please enter your age: ')
if age.isdigit():
   print('Nicely done!')
else:
   print('please use correct format!')

# At this point (up) we definitely while loop!

age = input('Please enter your age: ')
while not age.isdigit():
      print('Please use correct format')
      age = input('Try again!: ')
print('Nicely done!') 


for x in ['apple', 'orange', 'banana', 'grape', 'strawbery']:
   print(x) 
   
for x, item in enumerate (['apple', 'orange', 'banana', 'grape', 'strawbery']):
       print(x, ':', item)    

for x in range(1, 18):
   print(x)


fruites = ['apple', 'orange', 'banana', 'grape', 'strawbery']
i = 0
while i < len(fruites):
   print(fruites[i])
   if i == 2:
          print('we have enough fruits!')
          break
   i = i + 1
   
for x in ['apple', 'orange', 'banana', 'grape', 'strawbery']:
  print(x) 
  if x == 'banana':
         print('you have enough fruites!')
         break

vault = {'Fatih': 'Wr4563@@#$46est', 'Anne': 'We562462###st'} 
user = 'Fatih'
password = vault[user]
name = input('Please enter your name: ').lower().title()
if name == user:
    print(f'Hello {name}, your password is {password}')
else:
    print('Sorry, you are not authorized! ')
    
for i in (0, 1, 2, 3, 4, 5, 6):
    print(i)
    if i == 2:
        break

for i in (0, 1, 2, 3, 4, 5, 6):
    if i == 2 or i == 4:
        continue
    print(i) 
    print(10)


vault = {'Fatih': 'Wr4563@@#$46est', 'Anne': 'We562462###st'}

for key in vault:
    print(key)

for key in vault.keys():
    print(key)


for value in vault.values():
    print(value)
    
for key, value in vault.items():
    print(key, ':', value)
  
i = 0
while i < 4:
    i += 1
    print(i)



lst = ['alpha', 'bravo', 'charlie', 'delta', 'echo']

for s in lst:
    print(s[:1])


n = int(input('enter a number: '))

if n % 2 != 0:
    print('weird')
elif n % 2 == 0 and n in range(2, 5):
    print('not weird')
elif n % 2 == 0 and n in range(6,20):
    print('weird')
elif n % 2 == 0 and n > 20:
    print('Not weird')

cars = ['audi', 'Bmw', 'subaru', 'toyota']


for car in cars:
    if car.lower() == 'bmw':
        print(car.upper())
    else:
        print(car.title())


a= 3
print('A is positive number') if a > 0 else print ('A is a negative number')

