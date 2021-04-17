a = set('philadelphia')
b = set('fatihtepe')

print(a - b)
print(a.difference(b))

print(a | b)
print(a.union(b))

print(a & b) 
print(a.intersection(b))

day1 = {'04/16/2021'}
day2 = set('04/16/2021')

print(day1)
print(day2)

usa = set('washington')
nz = set('wellington')

print(usa.intersection(nz))
print(usa.difference(nz))
print(usa.union(nz))

if True:
    print('You can do that')


if False:
    print('nothing happened')



minced_meat = True
hamburger_bread = True
lettuce = True
pepper = False
grocery_store = True

ingredients = minced_meat and hamburger_bread and grocery_store \
    and (lettuce or pepper)
if ingredients:
    print('Bon Appetit!')




empty_seat = int(input('please enter a number: '))
if empty_seat >= 3:
    print('There is an empty seat for you')



s1 = set('TWELVE PLUS ONE')
s2 = set('ELEVEN PLUS TWO')
if s1 == s2:
    print("Two sets are equal")


convert = input('Please write Yes or No: ').lower().strip() == 'yes'
print('You entered: ', convert)


print('You entered: ', input('Please write Yes or No: ').lower().strip() == 'yes')


num = int(input('Please enter a number: '))
if num % 2 == 0:  
    print(f'The {num} is even')
else:
    print(f'The {num} is odd')


posneg_num = float(input('Please enter a number: '))
if posneg_num > 0:
    print('positive number is entered')
else:
    print('negative number is entered')


n1 = int(input('please enter a number: '))
n2 = int(input('Please enter another number: '))
if n1 > n2: 
    larger = n1
else:
    larger = n2
print('The larger number is:', larger)



n1 = int(input('please enter a number: '))
n2 = int(input('Please enter another number: '))
if n1 > n2:
    print('the larger nuber is', n1)
else:
    print('the larger number is', n2)


bool_value = True
if bool_value:
    print('Yes')
else:
    print('No')


first_num = int(input('Please enter a number: '))
second_num = int(input('Please enter another number: '))
third_num = int(input('Please enter last number: '))

if first_num > second_num and first_num > third_num:
    print(f'the largest number is {first_num}')
elif second_num > third_num and second_num > first_num:
    print(f'the largest number is {second_num}')
else:
    print(f'the largest number is {third_num}')



audience_group = 'kid', 'teen', 'adult'
audience = 'teen'

if audience in audience_group:
    if audience == 'kid':
        print('it is free to go to cinema')
    elif audience == 'teen':
        print('discounted price!')
    else: 
        print('normal price')
else:
    print('No such auidence, stay at home!')



score = int(input('Enter your score: '))

if score >= 90:
    if score >= 95:
        score_letter = 'A+'
    else:
        score_letter = 'A'
elif score >=80:
    if score >=85: 
        score_letter = 'B+'
    else:
        score_letter = 'B'
else:
    score_letter = 'Below B'
print('your score is %s' % score_letter)


gpa = float(input('What was your GPA?: '))
lowest_grade = float(input('What was your lowest grade?: '))

if gpa >= .85 and lowest_grade >= .70:
    honour_roll = True
else:
    honour_roll = False

if honour_roll:
    print("you made honour roll")
else:
    print('work hard next time!')


gpa = float(input('What was your GPA?: '))
lowest_grade = float(input('What was your lowest grade?: '))
if gpa >= .85 and lowest_grade >= .70:
    print("you made honour roll")
else:
    print('work hard next time!')


number = 0
while number < 6:
    print(number)
    number += 1
print(f'now, {number} is bigger or equal to 6')


my_list = ['a', 'b', 'c', 'd', 'e']
a = 0
while a < len(my_list):
    print('square of {} is: {}'.format(a, a**2))
    a += 1
    
    
    
answer = 11
question = ('Guess a number between 0 to 20: ') 
print("Let's play the guessing game!")

while True:
    guess = int(input(question))
    
    if guess < answer:
        print('little higher')
    elif guess > answer:
        print('little lower')
    else:
        print('You are a MINDREADER!')
        break
    

flowers = ['Rose', 'Orchid', 'Tulip']
count1 = len(flowers)
count2 = 0

while count1 > 0:
    print(flowers[count2])
    count1 -= 1
    count2 += 1
    print("count 1:", count1, "count2:", count2)
    print("end of {}th round".format(count2)+"\n")

a = 0

while a < 5:
    print('computer\'s gone creazy!')
    a += 1

while True:
    hello = input('How are you?: ')  # to exit hit q button.
    
    if hello == 'q':
        break    
    


hi = 1

while hi <= 3:
    hi += 1
    input('Are you ok?: ')
    print('bool value:', bool(hi <= 3))
    hi += 1
    input('Are you sure?: ')
    print('bool value:', bool(hi <= 3))
    hi += 1
    input('Really?: ')
    print('bool value:', bool(hi <= 3))
    print('Happy for you! I just wanna make sure your are ok!')


a = 0

while a < 10:
    a += 1
    if a % 2 == 0 or a % 2 == 1:
        print(a)            


for i in [1, 2, 3, 4, 5, 6, 7]:
    print(i)



seasons = ['sprint', 'summer', 'autumn', 'winter']
for season in seasons:
    print(season)


iterable = [1, 2, 3, 4, 5, 6, 7]
for i in iterable:
    print(i ** 2)


name = 'fatihtepe'
for i in name:
    print(i)


times = int(input('How many times shoul I say \'I love you\': '))

for i in range(times):
    print('I love you')



n = int(input('enter a number between 1-10: '))
for i in range(11):
    print('{}*{} = '.format(n, i), n * i)


b = list(range(11))
for i in b:
    print(i * 5)

a = set(range(10))
print(a)

print(*range(10, 0, -2))


text = ['one', 'two', 'three', 'four', 'five']
numbers= [1, 2, 3, 4, 5]
for x, y in zip(text, numbers):
    print(x, ':', y)



name = ['John', 'Anne', 'Bob', 'Alice']
title = ['Dad', 'Mom', 'Son', 'Doughter']
for n, t in zip(name, title):
    print(n, '==>', t)



who = ['John', 'Anne', 'Bob', 'Alice'] 
verb = ['is', 'is', 'is', 'is']
mood = ['happy', 'sad', 'depressed', 'great']
for i in who:
    for ii in verb:
        for iii in mood:
            print(i, ii, iii)

for w, v, m in zip(who, verb, mood):
    print(w, v, m)


a = 'fatihtepe'
print('h' in a) 

numbers = '123456789'

for i in numbers:
    if int(i) > 3:
        print(i)

tr_letters = "şçöğüİı"

password = input('your password: ')

for i in password:
    if i in tr_letters:
        print('You can not use Turkish letter in password')

