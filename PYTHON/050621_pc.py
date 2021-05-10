def is_prime_num(n):
    for i in range(2,  n // 2 + 1):
        if n % i == 0:
            return False
    return True

n = int(input('Enter a number: '))
listem = []

for x in range(2,n):
    if is_prime_num(x):
        listem.append(x)
print(listem)

n = int(input('Enter a number: '))
listem = []

for x in range(2,n):
    for i in range(2,  x // 2 + 1):
        if x % i == 0:
            break
    else:
        listem.append(x)
print(listem)

# prime number

def is_prime_num(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input('Enter a number: '))
listem = []

for x in range(2,n):
    if is_prime_num(x):
        listem.append(x)
print(listem)

# FizzBuzz
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, ': FizzBuzz')
    elif i % 3 == 0:
        print(i, ': Fizz')
    elif i % 5 == 0:
        print(i, ': Buzz')
    else:
        print(i)
    
for i in range(1, 101):
    s = ""
    if i % 3 == 0:
        s += "Fizz"
    if i % 5 == 0:
        s += "Buzz"
    if s == "":
        print(i)
    else:
        print(s)

a = 'I'
b = 'love'
c = 'you'

def texter(c, a, b):
    '''returns the reversed strign.'''
    print(a, b, c)
    
texter ('i', 'love', 'you')

print(texter.__doc__)

def who(first, last):
    print('the first name is', first)
    print('the last name is', last)
    
who('fatih', 'tepe')

# I love you
def texter(text1, text2, text3):
    print(f'{text2} {text3} {text1}')

texter(text1 = 'you', text2 = 'I', text3 = 'love')
texter('Ahmet', 'mehmet', 'fatih')


def brothers(bro1, bro2, bro3, bro4):
    print('I have brothers: ')
    print('here they are,', bro1, bro2, bro3, bro4, sep = '\n')
       
bros = ['fatih', 'tepe', 'orada', 'burada']

brothers(*bros)



geniuses = ('Bill', 'Rossum', 'Guido van', 'Gates')

def merger(par1, par2, par3, par4):
    print(f'For me, {par1} {par4} and {par3} {par2} are geniuses')

merger(*geniuses) 




def slicer(*args):
    print('evens: ', [i for i in args if i % 2 ==0])
    print('odd: ', [i for i in args if i % 2 != 0])
    
slicer(1, 2, 3, 5, 6, 6, 7, 9, 11, 23)


def fruiterer(*fruit):
    print('I want to get: ')
    for i in fruit:
        print('-', i)

fruiterer('orange', 'banana', 'melon', 'ananas')


def animals(**kwargs):
    for key, value in kwargs.items():
        print(value, 'are', key)

animals(Carnivores = 'Lions', Omnivores = 'Bears', 
        Herbivores = 'Deers', Nomnivores = 'Human')

def defa(**x):
    for t, z in x.items():
        print(t, 'is', z, 'years old.')

defa(ali = 33, sam = 45, john = 19, emily = 36)


def brothers(bro1, bro2, bro3):
    print('Here are the names of brothers: ')
    print(bro1, bro2, bro3, sep='\n')

family = ['tom', 'sue', 'tim']
brothers(*family)


def meaner(john, can, melinda):
    average = (john + can + melinda) / 3
    print('The average of ages is: ', average)
    
friends = {'john': 40, 'can': 30, 'melinda': 20}
meaner(**friends)

def positional_argument(a, b):
    print(a, 'is the firs argument.')
    print(b, 'is the second argument.')

positional_argument(35, 36)
print('>>>>>>><<<<<<<<<<')
positional_argument(36, 35)

def who(first, last):
    print('Your first name is: ', first)
    print('Your last name is: ', last)

who('Guido', 'van Rossum')
print('----------------')
who('Guido', last='van Rossum')
print('-----------------')
who(last = 'van Rossum', first ='Guido')
print('-----------------')
who(first = 'Robert', last ='van Rossum')