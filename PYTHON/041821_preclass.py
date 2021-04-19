# Admission for anyone under age 4 is free.
# Admission for anyone between the ages of 4 and 18 is $5.
# Admission for anyone age 18 or older is $10

age = int(input('what is your age?: '))
if age < 4:
    print('admission cost is $0!')
elif age < 18:
    print('admission cost is $5')
else:
    print('admission cost is $10')


num = int(input('Enter a number: '))
if num > 0:
    print(num, 'is positive')
    print(num, 'squared is', num * num)
else:
    print('it\'s negative')
print('Bye')


savings = float(input('Enter how much you have in savings: '))

if savings == 0:
    print("Sorry no savings")
elif savings < 0:
    print('Better start to save!!')
elif savings < 500:
    print('Well done')
elif savings < 1000:
    print('Thats a tidy sum')
elif savings < 10000:
    print('Welcome Sir!')
else:
    print('Thank you')

print('-' * 25)

snowing = False
temp = -1
if temp < 0:
    print('It is freezing')
    if snowing:
        print('Put on boots')
        print('Time for Hot Chocolate')
print('Bye')
print('-' * 18)

print('-' * 25)
age = 25
status = None
if age > 12 and age < 20:
    status = 'teenager'
else:
    status = 'not teenager'
print(status)


print('-' * 15)
age = int(input('enter age: '))
status = ('teenager' if age > 12 and age < 20 else 'not teenager')
print(status)

num = int(input('Enter a simple number: '))
result = (-1 if num < 0 else 1)
print('Result is', result)



number = int(input('enter a number: '))
i = 0
while i < number:
    print (i ** 2)
    i += 1
    

a = 3
while a**2 < 299:
    print('I will stop smoking')
    a += 3
    
    
total = 149
country = "FR"

if country == "FR":
    if total <= 50:
        print("Shipping Cost is  €30")
    elif total <= 100:
        print("Shipping Cost is €15")
    elif total <= 150:
        print("Shipping Costs €10")
    else:
        print("Free Shipping")
if country == "DE": 
    if total <= 50:
        print("Shipping Cost is  €25")
    else:
        print("Free Shipping")


ps4_price = 200
saved_amount = int(input('Please enter your saved amount: '))

if saved_amount <= ps4_price/2:
    print('You must save more, keep saving!')
elif saved_amount > ps4_price:
    print('Yippee! You can buy your PS4')
elif saved_amount > ps4_price/2:
    print('You save more than half, keep saving!')

math_mark = int(input('Please enter the mark: '))


if math_mark >= 85 and math_mark <= 100:
    print('A (Excellent)')
elif math_mark >= 70 and math_mark <= 84:
    print('B (Good)')
elif math_mark >= 60 and math_mark <= 69:
    print('C (Medium)')
elif math_mark >= 45 and math_mark <= 59:
    print('D (Not Bad)')
elif math_mark >= 0 and math_mark <= 44:
    print('F (Failed)')


a = 998
if a >= 999 :
    print(a ** 0)  

else :
    print(a * 2)

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
for day in range (len(weekdays)):
    print('Day', day+1, ':', weekdays[day])

number = int(input('Please enter a number: '))
i = 0
while i  < number:
    print(i ** 2)
    i += 1


sample_list = [{"section":5, "topic":2}, 'clarusway', 
               [1, 4], 2020, 3.14, 1+618j, False, (10, 20)]
for i in sample_list:
    print(f'The type of {i} is {type(i)}.')

a= [1,2,3,4]
b= [a[0:x+1] for x in range(0,len(a))]
c= [sum(a[0:x+1]) for x in range(0,len(a))]
print(b)
print(c)

a = []
for i in range(5):
    a.append(i)
print(a)


L1 = []
L1.append([1,[2, 3], 4])
L1.extend([7, 8, 9])
print(L1)
# print(L1[0][1][1])
# print(L1[2])

T = (1, 2, 3, 4, 5, 6, 7, 8,)
print(T[T.index(5)], end = ' ')
print(T[T[T[6]-3]-6])


set1 = {1, 2, 3}
set2 = set1.copy()  # here we copy set1 but later it does not affect set1
set2.add(4)
print(set1)
print(set2)


number = int(input('please enter a number: '))

if number < 0:
    print('it is negative number')
elif number > 0: 
    print('it is positive number')
else:
    print('The number you entered is 0')


number = int(input('please enter a number: '))

if number % 2 == 0:
    print('number is even')
else:
    print('number is odd')



distance_in_km_str = input('Please input the distance in kilometers:')

if distance_in_km_str.isnumeric():
    distance_in_km = int(distance_in_km_str)
    if distance_in_km < 1:
        print('You must enter a positive distance')
    else:
        print('You entered the distance', distance_in_km, 'in kilometers')
        distance_in_miles = distance_in_km * 0.6214
        print('The distance in miles is', distance_in_miles)
# else:
    print('Not an integer number')
