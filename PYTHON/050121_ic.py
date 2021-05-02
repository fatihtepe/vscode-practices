print(abs(-5))

a = "I"
b = "Love"
c = "You"
def texter(c,a,b):
  print(f"{a} {b} {c}")
texter(c,a,b)

def texter(a, b, c):
    print(f"{a} {b} {c}")
texter("i", "love", "you")


a = "I"
b = "Love"
c = "You"

def texter(c,a,b):
      print(f'{a} {b} {c}')
texter(c,a,b)


even_list= []
odd_list= []

def slicer(*slicer):
    for i in slicer:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    print(even_list)
    print(odd_list)

slicer(12, 3, 4, 6, 7, 9)
  

def animals(**kwargs):
    for key, value in kwargs.items():
        print(value, "are", key)
animals(Carnivores="Lions", Omnivores="Bears", Herbivores="Deers", Nomnivores="Human")



def organizer(**names):
    name = []
    age = []
    for key, value in names.items():
        name.append(key)
        age.append(value)
    print(name)
    print(age)
    
organizer(beth=26, oscar=42)


list_of_strings = ["5","6","7","8","9", "10"]
result = []

for i in list_of_strings:
    result.append(int(i))
print(result)



list_of_strings = ["5","6","7","8","9", "10"]
result = map(int, list_of_strings)
print(list(result))



list_of_strings = ["Ali","Veli","79","50","Clarusway", "10"]
# result = map(len, list_of_strings)

for i in (list_of_strings):
    if len(i) < 5:
        continue
    else:
        print(f'The word is {i} and its length {len(i)}')


def addition (n):
    return n * 2

list_of_strings = ["5","6","7","8","9", "10"]

new = map(int, list_of_strings)
new_list = list(new)
double = map(addition, new_list)
double_list = list(double)
print(double_list)



def squarely (a):
    return a * a

mylist = [2, 3, 4, 5, 6, 7, 7, 99]

newlist = map(squarely, mylist)
final_list = list(newlist)

for i in final_list:
    if i < 100:
        continue
    else:
        print(i)


list_of_strings = ['sat', 'bat', 'cat', 'mat']

tuplem = map(tuple, list_of_strings)
mytuple = tuple(tuplem)

print(mytuple)
print(mytuple[-2])

list_of_strings = ['sat', 'bat', 'cat', 'mat']
new = map(tuple, list_of_strings)
newtuple = list(new)
print(newtuple)


def absolute (num):
    '''this function returns the absolute
    value of the entered number'''
    if num >= 0:
        return num
    else:
        return -num
    
print(absolute(-25))
print(absolute.__doc__)



# first task
mylist = [5, 12, 17, 18, 24, 32, 999, 101]
def less_than_100(number):
    return number < 100

newlist = filter(less_than_100, mylist)
final_list = list(newlist)
print(final_list)


# second task
def filterWovels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    if letter.lower() in vowels:
        return True
    else:
        return False
    
sentence = 'I want to eat cake before dinner'
filtered_sentence = filter(filterWovels, sentence)
print(set(filtered_sentence))

# third task
mix_list = [5, 12, 17,'a', 'e', 'i', 24, 32,101] 

def less_than_ten(num):
    if type(num) == int and num <= 10:
        return True
    else:
        return False
    
filt_list = filter(less_than_ten, mix_list)
newlist = list(filt_list)
print(newlist)



mix_list = [5, 12, 17,'a', 'e', 'i', 24, 32,101] 
def find_string(s):
    if type(s) == str:
        return True
    else:
        return False
filtered_str = filter(find_string, mix_list)
str_list = list(filtered_str)
print(str_list)



mix_list = [5, 12, 17,'a', 'e', 'i', 24, 32,101] 
def which_are_str(x):
    if type(x) == str :
        return True
    else:
        return False
filt_list = filter(which_are_str, mix_list)
newlist = list(filt_list)
print(sorted(newlist, reverse = True))



mylist = [5, 12, 17, 18, 24, 32, 999, 101, 1, 9]
def less_than_ten(num):
    if num <= 10:
        return True
    else:
        return False
filt_list = filter(less_than_ten, mylist)
newlist = list(filt_list)
print(newlist)


def listint(num):
    if num < 10:
        return True
    else:
        return False
mix_list = [5, 12, 17, 18, 24, 32, 999, 101, 1, 9] 
filtlist = filter(listint, mix_list)
newlist = list(filtlist)
print(newlist)

