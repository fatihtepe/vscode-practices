sentence = input('give me a sentence: ')
words = sentence.split()
i = 0
longest = 0
while i < len(words):
    if len(words[i]) > longest:
        longest = len(words[i])
    i += 1
print(f'The longest word\'s length is {longest}')
        
        
        
names = ['Ahmed', 'Aisha', 'Adam', 'Joseph', 'Gabriel']
 
for i in names:
    print(f"Hello {i}")  

names = ["Ahmed", "Aisha", "Adam", "Joseph", "Gabriel"]
prefix = "Hello "
i = 0
a = len(names)
while i < a :
    print(prefix, names[i])
    i += 1



liste = []
for i in range(1, 6):
    liste.append(i)
print(liste)

input = 'Clarusway'
for i in range(len(input)):
    if i == len(input) - 1:
        print(input[i], end = '')
    else:
        print(input[i], end = "-")
        
word = input('give me a word')


sayac = 0
for i in word:
    sayac += 1
    if sayac < len(word):
        print(i, end='-')
    else:
        print(i, end='')
    
    
word = "clarusway"
a = "-".join(word)
print(a)


user = {"name": "Daniel", "surname": "Smith", "age": 35}
for item in user.items():
    print(item)

for key, value in user.items():
    print(key, '=>', value  )

for key, value in user.items():
    print(value)
 
for key in user.keys():
    print(key)
for value in user.values():
    if value == 'Daniel': 
        print(len(value))

print(user['name'])

'''Samanlikta igne arayalim mi?'''

samanlik = ['yumurta', 'yaba', 'saman', 'tirmik', 'igne', 'tezek']
print(f'igne {samanlik.index('igne')} numarali intexte.')

'''Tuple kullanarak coklu deger assign etmek'''

v = ('five', 5, True)
(x, y, z) = v
print(x, y, z)


a, b, c = 1, 2, 3

monday, tuesday, wed, thurs, fri, satur, sunday = tuple(range(1, 8))
print(monday)


print([1, 2, 3, 4] + ['11', '22', 33])

tt = (1, 2, [1, 3, 5])
tt[2].append(4)
print(tt)


x, y = (10, 20, 40, 60)
print(x)
print(y)

x = 10


a, _, b, _ = (10 , 20 ,40, 50)
print(a, b)


x, y, *z = (11, 22, 33, 44, 55)
print(z)


x, y, *_ = (11, 22, 33, 44, 55) 
print(x, y, *_)


'''Working with the iterators'''


number = int(input('give me a number between 1-10: '))
for i in range(11):
   print('{} x {} ='.format(number, i), number * i)



name = ['tarik', 'numan', 'selim']
age = [11,  22, 33]

xx = zip(name, age)
print(list(xx))

for x, y in xx: 
    print(x, y)

l=list('HELLO')
p=l[0], l[-1], l[1:3]
print('a={0}, b={1}, c={2}'.format(*p))


l=list('HELLO')
p=l[0], l[-1], l[1:3]
print('a={0}, b={1}, c={2}'.format(*p))

times = int(input('gimme a nuber: '))

for i in range(times):
    print('I love you')


num = int(input('write a number between 1-10: '))
for i in range(11):
    print('{} X {} = {}'.format(i, num, num * i))
    
    
seq = range(5)
for i in seq:
    print(i)

nl = []
for i in range(1500, 2700):
    if (i % 7 == 0) and (i % 5 == 0):
        nl.append(str(i))
print(',' .join(nl))




