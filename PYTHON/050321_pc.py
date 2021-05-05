def sum_double(x, y):
    if x != y:
        return x + y
    else:
       return (x  + y) * 2  

print(sum_double(5, 8))
print(sum_double(3, 3))


x = [True, True, False, 0, 45, '']
if any(x):
    print("At least one True")
if all(x):
    print("Not one False")
if any(x) and not all(x):
    print("At least one True and one False")


dictionary = {"a": 1, "b": 2}
def someFunction(a, b):
    print(a + b)
    return
# these do the same thing:
someFunction(**dictionary)
someFunction(a=1, b=2)


numbers = [1,2,3,4,5,6,7]
evens = [x for x in numbers if x % 2 == 0]
odds = [y for y in numbers if y not in evens]


cities = ['London', 'Dublin', 'Oslo']
def visit(city):
    print("Welcome to " + city)
    
for city in cities:
    visit(city)



x = [True, True, False, 0, 45, '']
for i in range(len(x)):
    print(x[i], i)



x = [True, True, False, 0, 45, '']
i = 0
while i < len(x):
    print(x[i], i)
    i += 1    


x = [True, True, False, 0, 45, ''] 
for index, element in enumerate(x):
    print(element, index)


x = [True, True, False, 0, 45, ''] 
newlist = enumerate(x)
print(list(newlist))

    
x = [True, True, False, 0, 45] 
y = []
for i in enumerate(x):
    y.append(i)
print(y)
        
        
grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)
print(type(enumerateGrocery))
print(list(enumerateGrocery))



grocery = ['bread', 'milk', 'butter']
for index, item in enumerate(grocery):
    print(index, item)


grocery = ['bread', 'milk', 'butter']
for count, item in enumerate(grocery, start=1):
    print(count, item)
    

items = [8, 23, 45, 12, 78]
for i in enumerate(items):
    print("index/value", i)


'''For example, let's say we need to create a 
list of integers which specify the length of 
each word in a certain sentence, but only if 
the word is not the word "the".'''




num = 1
while num <= 10:
    print(num)
    num += 1



dictionary_tk = {
  "name": "Leandro",
  "nickname": "Tk",
  "nationality": "Brazilian",
  "age": 24
}
for key, value in dictionary_tk.items():
    print('My %s is %s' %(key, value))



def check_prime(number):
    for x in range(2, int(number ** 0.5) + 1):
        if number % x == 0:
            return False
    return True

print(check_prime(19))


def check_bra(a):
    key_value = {'(': ')', '[':']', '{':'}'}
    open_brac = set(['(', '[', '{'])
    list_1 = []
    for i in a:
        if i in open_brac:
            list_1.append(i)
        elif list_1 and  i == key_value[list_1[-1]]:
            list_1.pop()   
        else:
            return False
    return list_1 == []
bracelets = input("please enter bracelets correct way: ")
print(check_bra(bracelets))



