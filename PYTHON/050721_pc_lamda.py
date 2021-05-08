add = lambda x, y : x + y

print(add(2, 3))
print(type(add))


def square(x):
    return x ** 2

map(square, [1, 2, 3, 4, 5, 6])
print(list(map(square, [1, 2, 3, 4, 5, 6])))
print('-------------------------------')
squarelist = map(square, [1, 2, 3, 4, 5, 6])
print(list(squarelist))


map(lambda x : x ** 2, [1, 2, 3, 4, 5, 6])
print(list(map(lambda x : x ** 2, [1, 2, 3, 4, 5, 6])))


list_odd = [1, 3, 5, 7, 9]
list_even = [2, 4, 6, 8, 10]
  
map(lambda x, y: x + y, list_odd, list_even)

total = list(map(lambda x, y: x + y, list_odd, list_even))
print(total) 
print('------------------')
print(list(map(lambda x, y: x + y, list_odd, list_even)))

listem = [4, 5, 7, 8, 9, 80, 56, 45, 46, 70, 30, 35]

filter(lambda x : x % 2 == 0, listem)

odd_listem = list(filter(lambda x : x % 2 != 0, listem))
print(odd_listem)
print('------------------')
print(list(filter(lambda x : x % 2 != 0, listem)))


listem = [4, 5, 7, 8, 9, 80, 56, 45, 46, 70, 30, 35]

filter(lambda x: x % 2 == 0, listem)
print(filter(lambda x: x % 2 == 0, listem))
# returns <filter object at 0x104702a00>

print('----------------------')

even_listem = tuple(filter(lambda x: x % 2 == 0, listem)) 
print(even_listem)
# you can convert it tuple, list etc.


def parrot_trouble(talking, hour):
    if talking and (hour < 6 or hour > 21):
        return True
    else:
        return False

print(parrot_trouble(True, 5))


def not_string(word):
    if word.startswith('not'):
        return word
    else:
        return 'not ' + word
    



def missing_char(word, n):
    return word[:n] + word[n+1:]

print(missing_char('kitchen', 1))



sentence = "where is the brave new world"
for i in sentence:
  if i =="e" or i=="w":
    continue
  else:
    print(i)



given_list =[5, 4, 4, 3, 1, -2, -3, -5 ]
sum = 0
for i in given_list:
  if i>0:
    sum+=i
print(sum)


# Prints all letters except 'e' and 'w'
sentence = 'where is the brave new world'
for i in sentence:
    if i != 'e' and i != "w":
        print(i, end="")



# Find the sum of all negative numbers
given_list =[5, 4, 4, 3, 1, -2, -3, -5 ]
sum_neg = []
sum_poz = 0
for i in given_list:
    if i<0:
        sum_neg.append(i)
    else:
        sum_poz += i
print(sum_neg)
print(sum_poz)


# The function should be created in such a way that it will work for both lists, 
# tuples and sets.
def mult_to_mult(paramatre):
    result = 1
    for i in paramatre:
        result = result * i
    return result
list_of_tuple = (1, 2, 3, 4)
print(mult_to_mult(list_of_tuple))
list_of_list = [1,2,3,4,5,6, 7]
print(mult_to_mult(list_of_list))



#Write a function called duplicateEliminator that takes in a list, 
# eliminates any duplicate values, and returns a set.
# def duplicateEliminator (paramater):
#    return set(paramater)
list_1 = [1,12, 13, 4, 12, 23, 44, 13, 45, 1, 2, 3, 4, 173, 23, 44, 44, 44, 44]   
print(set(list_1))      # easy solution
# if we want to return list 
def duplicateEliminator_2(param):
    temp_list = []
    for i in param: 
        if i not in temp_list:
            temp_list.append(i)
    return temp_list        
print(duplicateEliminator_2(list_1))



#With lambda function combine first name and last name into a single "Full Name" 
firs_name = 'Joseph'
last_name = 'Eric'
full_name = lambda a, b : a + " " + b
print(full_name(firs_name, last_name))



 #Find the movies start with letter "G". use List Comprehension.
movies = ["Star Wars","Gandhi","Casablanca",
"Gone with The Wind","The Wizard of Oz","To kill a Mockingbird",
"Ghostbusters","Gattaca"]
for i in movies:
    if i[0]=="G":
        print(i)
print([x for x in movies if x[0]=="G"])



#List Comprehension : IF-ELSE
#convert text of each item of list to uppercase letters 
# if length of string is greater than 4. 
# Otherwise, convert text to lowercase
list_sent = ['aLi', 'caGRi', 'DaviD', 'faTmA', 'soFIa', 'HavA', 'NuR', 'buSRA']
a = [x.upper() if len(x)>4  else x.lower()  for x in list_sent ]
print(a)