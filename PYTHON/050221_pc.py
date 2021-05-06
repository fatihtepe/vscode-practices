def listem():
    print('hello')
listem()


def filterVowels(letter) :
    vowels = ["a", "e", "i", "o", "u"]
    if letter.lower() in vowels :
        return True
    else :
        return False
sentence = 'I have been there couple times'
print(set(filter(filterVowels, sentence)))


print(filterVowels('b'))


def absolute(num) :
    """
This function returns the absolute
value of the entered number
    """
    if num >= 0 :
        return num
    else:
        return -num
print(absolute.__doc__)


def positional_argument(a, b):
    print(a, 'is the first argument')
    print(b, 'is the second argument')

positional_argument('Tarik', 'Jackhal')


def concat(a, b):
    print(a + b)
    
concat('Waterloo ', 'Kitchener')

a = 'Toronto'
b = 'Ottowa'
concat(a, b)
concat('London ', b)

def default(a = "John", b = 33) :
    print(a, "is", b, "years old.")
    
default('Mahir', 45)
default()


def parrot(voltage, state="a stiff", action="voom", typed="Norwegian Blue"):
    print("-- This parrot wouldn't", action, end=" ")
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", typed)
    print("-- It's", state, "!")

parrot(1000, action = 'zooom')


def oddevener(*num):
    print('Even numbers: ', [i for i in num if i % 2 == 0])
    print('Odd numbers: ', [i for i in num if i % 2 == 1])
    
oddevener(0, 4, 5, 6, 8, 9, 23, 34, 45, 66)

print('---------------------------------------')

def description(**staff):
    for key, value in staff.items():
        print(key, 'is', value, 'years old.')

description(Ali = 45, John = 43, Emilly = 23)



lst = [1, 2, 3, 4, 5]
for i in range(len(lst)):
     print(lst[i])
    
     
for j in range(0,10):
    print(j, end = " ")



a = 'i'
b = 'love'
c = 'you'
def texter(c, a, b):
    print(f'{a} {b} {c}')

texter(c, a, b)


numList = ['1', '2', '3', '4']
separator = '$ '
print(separator.join(numList))


name = ['f', 'a', 't', 'i', 'h']
sep = ''
print(sep.join(name))


def increment(number, another, by=1):
    return number + another + by


print(increment(2, 3, 5))


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply(3, 4, 5, 55, 7))


def save_user(**user):
    print(user)

save_user(id = 1, name = 'Fatih', age = 45 )


def save_user(**user):
    for key, value in user.items():
        print(key, '==>', value)

save_user(id = 1, name = 'Fatih', age = 45 )


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return 'FizzBuzz'
    if input % 3 == 0:
        return 'Fizz'
    if input % 5 == 0:
        return 'Buzz'
    return input
        
print(fizz_buzz(7))


secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('you won!!!')
        break
else:
    print('Sorry, you failed!')


command = ''
started = False
while True:
    command = input('> ').lower()
    if command == 'start':
        if started:
            print('Car is already started!')
        else:
            started = True
        print('Car started...')
    elif command == 'stop':
        if not started:
            print('Car is already stopped!!')
        else:
            started = False
        print('car stopped.')
    elif command == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to quit
              ''')
    elif command == 'quit':
        break
    else: 
        print('Sorry, I don\'t understand that!')