allistem = all(["", "dolu", 1])
print(allistem)


ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)


listem = [None, "0", "istanbul", ()]
filtered = filter(None, listem)
print(*filtered)

for i in filtered:
    print(i)


seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))


print(min('fatih'))

print(ord('f'))
print(ord('a'))
print(ord('t'))
print(ord('i'))
print(ord('h'))

print(max('fatih'))


print(sum([1,2,3,4,5]))


def add(a, b):
    print(a + b)

add(5, 15)    


def calculator (a, b, opr):
    if opr == '+':
        print(a + b)
    elif opr == '-':
        print(a - b)
    elif opr == '*':
        print(a * b)
    elif opr == '/':
        print(a / b)
    else:
        print('Enter a valid operator!')
        
calculator(5, 5, '-')


def toplama(a, b):
    return a + b
print(toplama(2, 5))



def string():
    return 'fatih'
print(string())
print(type(string()))


def listem() :
    return [1,2,3,4,5]
print(listem())

for i in listem():
    print(i)





