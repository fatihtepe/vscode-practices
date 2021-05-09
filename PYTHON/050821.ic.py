words1=["you", "much", "hard"]
words2=["i", "you", "he"]
words3=["love", "ate", "works"]

sentence = map(lambda x, y, z : x + ' ' + y + ' ' + z, 
               words2, words3, words1)
 
for i in sentence:
    print(i)




words = ['apple', 'swim', "clock", "me", "kiwi", "banana"]

for i in filter(lambda x : len(x) < 5, words):
    print(i)



first_ten=set("abcdefghij")
sesli=set("aeoöuüıi")

vowels = filter(lambda x: x in sesli, first_ten)

print(list(vowels))



def modular_function(n):
    return lambda x: x ** n

power_of_2 = modular_function(2)  # first sub-function derived from def
power_of_3 = modular_function(3)  # second sub-function derived from def
power_of_4 = modular_function(4)  # third sub-function derived from def
print(power_of_2(2))  # 2 to the power of 2
print(power_of_3(2))  # 2 to the power of 3
print(power_of_4(2))  # 2 to the power of 4



def repeater(n):
    return lambda x: x * n

repeat2times = repeater(2)
print(repeat2times('fatih'))


def functioner(emoji = None):
    return lambda message : print(message, emoji)

myprint_smile = functioner(':)')
myprint_smile([66])

print_uzgun = functioner(':(')
print_uzgun('bugunku dersteki yuz ifadem -->')



import math 


print(dir(math))


from math import pi, log10, factorial

print(pi)
print(log10(1000))
print(factorial(4))


import string as str

print(str.punctuation)
print(str.digits)


import datetime

print(datetime.date.today())
print(datetime.datetime.now())




from datetime import date

birth = date(571, 4, 2)
death = date(632, 6, 8)

days = date.toordinal(death) - date.toordinal(birth)
print(days)


from random import choice
paths = ['Data Science', 'DevOps', 'Full Stack']
print(choice(paths))


import random

# Are you ready for choice your path
# best wishes ---- mehmetfatihdata
path = ['Data Science', 'DevOps/AWS', 'Full Stack']
ch = []
count = 0
while count < 100:
    ch.append(random.choice(path))
    count += 1
DS_say = []
DO_say = []
FS_say = []
for i in ch:
    if i == 'Data Science':
        DS_say.append(i)
    elif i == 'DevOps/AWS':
        DO_say.append(i)
    else:
        FS_say.append(i)
        
DataScience = " % " + str(len(DS_say)) + " Your Path is " + "DataScience"
DevOpsAWS = " % " + str(len(DO_say)) + " Your Path is " + "DevOpsAWS"
FullStack = " % " + str(len(FS_say)) + " Your Path is " + "FullStack"
print(
    f' Canguralations and reinvent yourself. ******\
{max(DataScience, DevOpsAWS, FullStack)}******'
)


def factor(x):
    
    result = 1
    for i in range(x):
        result *= (i+1)
    return print(result)


factor(4)


result = 1

for i in range(1, 5):
    result *= i
print(result)



from random import choice

city = ['Stockholm', 'Istanbul', 'Seul', 'Cape Town']
print(choice(city))  



import random 

city = ['Stockholm', 'Istanbul', 'Seul', 'Cape Town']
print(random.choice(city))  
print(random.random())  # generates random float nubers range of (0, 1)


def my_function_1(a, b):
    area = a * b
    return area

def my_function_2(a, b):
    hypotenuse = (a**2 + b**2)**0.5
    return hypotenuse

area = my_function_1(10, 20)
print(area)
hypotenuse = my_function_2(30, 40)
print(hypotenuse)


num1 = [9, 6, 7, 4]
num2 = [3, 6, 5, 8]

numbers = map(lambda x, y: (x + y)/ 2, num1, num2)

print(list(numbers))



words1=["you", "much", "hard"]
words2=["i", "you", "he"]
words3=["love", "ate", "works"]

sentence = map(lambda x, y, z: x + ' ' + y + ' ' + z, words2, words3, words1)
for i in sentence:
    print(i)


words = ['apple', 'swim', "clock", "me", "kiwi", "banana"]
for i in filter(lambda x: len(x) < 5, words):
    print(i)



vowels_list = ['a', 'i', 'e', 'o']
first_ten = ['a', 'c', 'd', 'f', 's', 'm', 'e']
vowels = filter(lambda x: True if x in vowels_list else False, first_ten)

print(list(vowels))



vowels_list = ['a', 'i', 'e', 'o']
first_ten = ['a', 'c', 'd', 'f', 's', 'm', 'e']
vowels = filter(lambda x: x in vowels_list, first_ten)

print(list(vowels))


def modular_function(n):
    return n ** 2
print(modular_function(2))


power_of_2 = lambda x: x ** 2
print(power_of_2(2))


def modular_function(n):
    return lambda x: x ** n

lambda_power_2 = modular_function(2)

print(lambda_power_2(5))


def repeater(n):
    return lambda x: x * n

l = repeater(5)
print(l('fatih '))



def functioner(emoji):
    return lambda x: x + emoji

smile = functioner(' :))')
print(smile('hello'))
sad = functioner(' :((')
print(sad('hello'))
neutral = functioner(': |')
print(neutral('hello'))



(lambda x : print(x))(33 + 22)



def numan(n):
    return lambda x: x ** n

power5 = numan(5)

print(power5(15))



x = [24, 6, 56, 10]
y = [22, 44, 44, 60]
z = [32, 10, 50, 50]

ortalama = list(map(lambda x, y, z: (x + y + z) / 3 , x, y, z))
print(ortalama)
print('-------------***------------')

l = lambda x, y, z: (x + y + z) / 3
ortalama = list(map(l, x, y, z))
print(ortalama)


def func(x):
    return x + 2
print(func(5))



def func_generator(n):
    return lambda x : n(x)

fatih_print= func_generator(print)
fatih_print('neutral')

fatih_max = func_generator(max)
print(fatih_max([45, 15, 9]))


def repeater(n):
    return lambda x: x * n

five_repeat = repeater(5)
print(five_repeat('Clarusway! '))



def powerer(n):
    return lambda x: x ** n

power3 = powerer(3)
print(power3(5))
print('***********************')
power2 = powerer(2)
print(power2(8))


def i_function(n):
    return lambda x: n(x)

print('--------------------------')

i_print = i_function(print)
i_print('with i_print we used print function')
i_print('***********************')

i_bool = i_function(bool)
x = 5
y = 10
i_print(i_bool(x == y))
i_print('***********************')

i_max = i_function(max)
listem = [1, 3, 5, 99, 11]
i_print(i_max(listem))
print('------------------------')

def emojer(n):
    return lambda x: x + n

smile = emojer(' :))')
print(smile('I am happy'))

print('------------------------')

sad = emojer(' :((')
print(sad('I am sad'))
