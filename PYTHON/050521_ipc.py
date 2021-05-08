def organizer(**names):
    name = []
    age = []
    for key, value in names.items():
        name.append(key)
        age.append(value)
    print(name)
    print(age)
    
organizer(Beth = 26, Oscar = 45, Fatih = 44)



def organizer(**names):
    for key, value in names.items():
        print(key, 'is', value, 'years old')
     
organizer(Beth = 26, Oscar = 45, Fatih = 44)



x = lambda a, b, c : a + b + c
print(x(5, 6, 2))



oddeven = lambda x: 'odd' if x % 2 != 0 else 'even'
print(oddeven(45))
 
 
print((lambda x, y: (x + y) / 2)(3, 5))




iterable = [1, 2, 3, 4, 5]
map(lambda x: x ** 2, iterable )
print(list(map(lambda x: x ** 2, iterable))
      
      
 
iterlist = [1, 2, 3, 4, 5]     
result = map(lambda x: x ** 2, iterlist) 
print(list(result))


mylist = [2, 3, 4, 5, 6, 8, 29]
print(list(map(lambda x: x ** 2, mylist)))



letter1 = ['o', 's', 't', 't']
letter2 = ['n', 'i', 'e', 'w']
letter3 = ['e', 'x', 'n', 'o']

print(list(map(lambda x, y, z: x + y + z, letter1, letter2, letter3)))


first_ten = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
even = filter(lambda x : x % 2 == 0, first_ten)

print(list(even))


vowel_list = ['a', 'e', 'i', 'o', 'u']
first_ten = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

vowels = filter(lambda x: True if x in vowel_list else False, first_ten)
print(f'The vowels are {list(vowels)}.')


def repeater (n):
    return lambda x: x * n

two_times = repeater(2)
print(two_times('fatih '))



def modular_function(n):
    return lambda x: x ** n

power_of_3 = modular_function(3)
print(power_of_3(5))


print((lambda x: x**3)(5))

mean = lambda x, y: (x+y)/2
print(mean(8, 10))


multiply = lambda x: x * 4
add = lambda x, y: x + y
print(add(multiply(10), 5))

number_list = [1, 2, 3, 4]
result = map(lambda x:x**3, number_list)
print(list(result)) 


number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] 
divisible_list = filter(lambda x:x%3==0, number_list) 
print(list(divisible_list))

square = lambda x : x ** 2
print(square(2))


number_list=[1, 2, 3, 4, 5]
result= list(map(lambda x: x ** 2, number_list))
print(result)


number_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result= list(filter(lambda x: x % 2 != 0, number_list))  


square = lambda x : x ** 2


number_list=[1, 2, 3, 4, 5]
result= list(map(lambda x: x ** 2, number_list))

number_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result= list(filter(lambda x: x % 2 != 0, number_list)) 

def brothers(bro1, bro2, bro3):
    print('Here are the names of brothers :')
    print(bro1, bro2, bro3, sep='\n')
family = ['tom', 'sue', 'tim']

brothers(*family)


def sugar(x, y, z, d):
    print('This are stocked fruits: ')
    print(x, y, z, d, sep = '\n')

fruits = ['apple', 'orange', 'pear', 'banana']

sugar(*fruits)


def gene(x, y):  # defined by positional args
    print(x, "belongs to Generation X")
    print(y, "belongs to Generation Y")

dict_gene = {'y' : "Marry", 'x' : "Fred"}
gene(**dict_gene)  # we call the function by a single argument(variable)

def gene(x, y): 
    print(x)
    print(y)

dict_gene = {'y' : "Marry", 'x' : "Fred"}
gene(**dict_gene)  


def gene(x = 'Solomon', y= 'David'):  
    print(x, "belongs to Generation X")
    print(y, "belongs to Generation Y")
dict_gene = {'y' : "Marry", 'x' : "Fred"}
gene(**dict_gene)  
print('--------')
gene()


def couples(bride, groom):
    couples_list = []
    for x in zip(bride, groom):
        couples_list.append(x)
    return couples_list

dict_couple = {'bride': ['Marry', 'bella', 'linda'],
               'groom':['rye', 'fred', 'rolan']}
print(couples(**dict_couple))



def couples(bride, groom):
    return [x for x in zip(bride, groom)]

dict_couple = {'bride': ['Marry', 'bella', 'linda'],
               'groom':['rye', 'fred', 'rolan']}
print(couples(**dict_couple))



friends = {"AhmEt" : 44, "JOSePH" : 39, "LiNDa" : 55}
def meaner(AhmEt, JOSePH, LiNDa):
    average = (AhmEt + JOSePH + LiNDa) / 3
    print("The average of their ages is :", average)
print(meaner(**friends))

'''Workshop quesiton 1 solution'''
def query(s):
    while "()" in s or "{}" in s or '[]' in s:
        s = s.replace("()", "").replace('{}', "").replace('[]', "")
    return s == ''
print(query('()'))



'''lambda'''
lambda x: 'odd' if x % 2 else 'even'



listem = [1, 2, 3, 4]

for i in listem:
    print(i, ':',  (lambda x: 'odd' if x % 2 else 'even')(i))



hipotenus = lambda a, b: (a**2 + b**2) ** 0.5
print(hipotenus(3, 4))





iterable = [1, 4, 5, 6]

def karesinial(x):
    return x ** 2
result = map(karesinial, iterable)
print(*result)


letter1 = ['o', 's', 't', 't']
letter2 = ['n', 'i', 'e', 'w']
letter3 = ['e', 'x', 'n', 'o']

print(list(map(lambda x, y, z: x + y + z, letter1, letter2, letter3)))


letter1 = ['o', 's', 't', 't']
letter2 = ['n', 'i', 'e', 'w']
letter3 = ['e', 'x', 'n', 'o']

letter = map(zip, letter1, letter2, letter3)

for i in letter:
    for j in i:
        print(j)