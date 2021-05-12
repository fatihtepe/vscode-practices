# for multiplication and exponentiation

print( 8 * 8 )

print('**********')

print( 8 ** 2)



# Arguements

def instructors (*names):
    print(type(names))
    for n in names:
        print(n)

instructors('Micheal', 'Joseph', 'Robert', 'John', 'Marcus')



def instructors (**names):
    print(type(names))
    for key, value in names.items():
        print(key, value)
        
instructors(Python = 'Micheal', Pythoney = 'Joseph', Git = 'Robert')



# Iterable Unpacking

listem = [1, 2, 3]
tuplem = (4, 5, 6)
setim = {7, 8, 9}
benim = [*listem, *tuplem, *setim]

print(f'My new list ===> {benim}')


# upacking dict
mydict = {'a': 8, 'b': 9, 'c': 10}  
print(*mydict)

print('{a} {b} {c}'.format(**mydict))




# Bonus!

listem = [1, 2, 3, 4 , 5, 6, 7, 8]
*a, b = listem

print(a)
print(b)












# play ground
def mixed(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])
        
mixed(1,2, 3, 4, 5, 6, seven = 8, eight = 9)


def pack(a, b, c):
    print(a, b, c)
    
mylist = [1, 2, 3,]  # upacking lists
pack(*mylist)

mydict = {'a': 8, 'b': 9, 'c': 10}  # upacking dict
pack(**mydict)



x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = []

for i in x:
    if i % 5 == 0:
        y.append(i)
print(y)


y = [i for i in x if i >= 5]
print(y)


z = lambda x: x ** 2
l = [3, 4, 5, 6, 7, 8]
ebru = list(map(z, l))
print(ebru)


