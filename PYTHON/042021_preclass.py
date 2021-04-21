'''Task:
You will be given an array of numbers. You have to sort the odd 
numbers in ascending order while leaving the even numbers at 
their original positions.'''

numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] 
odd = []
numbers_new = []

for i in numbers:
    if i % 2 == 1:
        odd.append(i)
    odd.sort(reverse=True)
for i in numbers:
    if i % 2 == 1:
        numbers_new.append(odd[-1])
        odd.pop()
    else:
        numbers_new.append(i)
print(numbers_new)





# initialize the list of an integer array representing the elevation, and set it to empty
height = []
# Unless user types `ok`, get input of numbers from the user
while True:
    num = input("Type 'ok' when you are done: ")
    # if the input is not equal to `ok`, add the input number to the height array
    if num != "ok":
        height.append(int(num))
    # if the input equals to `ok`, get out of the while loop
    else:
        break
# initialize areas which holds total amount of water to be trapped, and set to 0
areas = 0
# initialize maximum left and right, and set to 0
max_l = max_r = 0
# initialize left, and set to 0
l = 0
# initialize right and set to the last index of the input array
r = len(height)-1
# unless the current position of the height on left
# is not greater than the one on right, run the loop
while l < r:
    # if the current position on left is lower than the right,
    # max level on left determines the amount of water to be trapped.
    if height[l] < height[r]:
        # if the current height on left is greater than max height on left
        # then the water not to be trapped, and set the max height to the new max
        if height[l] > max_l:
            max_l = height[l]
        # otherwise, add the amount of water to be trapped.
        else:
            areas += max_l - height[l]
        # increase current position on left by one
        l += 1
    # if the current position on left is higher than the right,
    # max level on right determines the amount of water to be trapped.
    else:
        # if the current height on right is greater than max height on height
        # then the water not to be trapped, and set the max height to the new max
        if height[r] > max_r:
            max_r = height[r]
        # otherwise, add the amount of water to be trapped.
        else:
            areas += max_r - height[r]
        # decrease current position on right by one
        r -= 1
# print the amount of water to be trapped
print("\nRain-trapped area : ", areas)



''' Coding Challenge-2 : Group Anagrams

Purpose of the this coding challenge is to solve a grouping algorithm in Python.

### Learning Outcomes

At the end of the this coding challenge, students will be able to;

- get a basic understanding of grouping algorithms.
- demonstrate their knowledge of lists, dicts in python
- implement loops to solve the problems in python
- get a better understanding of computational thinking concepts

### Problem Statement
  
- Given a list of strings, group anagrams together.

- Example:

**Input:**
```
["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```
Note:
All inputs will be in lowercase.
The order of your output does not matter.'''

strs = ["eat", "tea", "tan", "ate", "nat", "bat", "cat", "tac"]
anag = {}
for i in strs:
    element = "".join(sorted(i))
    if element in anag:
        anag[element].append(i)
    else:
        anag[element] = [i]
print(list(anag.values()))


'''Second Solution'''

liste = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
sorted_list = []
sonuc = []
for i in liste:
  if sorted(i) not in sorted_list:
    sorted_list.append(sorted(i))
for a in range(len(sorted_list)):
  sonuc.append([i for i in liste if sorted(i)==sorted_list[a]])
print(sonuc)



'''## Coding Challenge-1 : Find the Largest Number

Purpose of the this coding challenge is to solve a simple sorting problem in Python.

### Learning Outcomes

At the end of the this coding challenge, students will be able to;

- get a basic understanding of sorting algorithms.
- demonstrate their knowledge of lists in python
- implement loops to solve the problems in python
- get a better understanding of computational thinking concepts

### Problem Statement
  
- Write a python code that finds the largest number among 
the ``n`` numbers given by the user as input.

- First, take `n` from the user, then take `n` numbers one 
by one and select-print the largest one.

- It is forbidden to use ``max()`` function.  

- Indicate which computational thinking concepts have you used.

- Example for user inputs and respective outputs
```text
Input                Output
---------------:     -------------------------:
n = 5, 1 2 3 4 5     The largest number is:  5
n = 3, 67 85 19      The largest number is:  85'''

a = int(input("How many numbers will you enter ?"))
values = []
i = 1
while i <= a:
    values.append(int(input("enter a value: ")))
    i += 1
print(values)
print(sorted(values))
print("The largest number is :", sorted(values)[-1])


numbers = []
i = 0
while i <= len(numbers):
    numbers.append(int(input('enter a number: ')))
    i += 1
    if i == 5:
        break
print(numbers)
print(sorted(numbers))
print(f'The largest number is {sorted(numbers)[-1]}')


numbers = [int(input("enter a number: ")) for i in range(5)]
print(numbers)
print(sorted(numbers))
print(f'The largest number is {sorted(numbers)[-1]}')


sucesessish = {'pre-class', 'in-class'}
success = {'pre-class', 'in-class', 'practice'}
print(f'To be more successful do more {success.difference(sucesessish)}')


my_name = 'Tarik'
first_name = input('Enter your name: ').lower().title()
if first_name == my_name:
    print(f'Helllo, {my_name}! The password is : W@12')
else:
    print('Access denied!')


title = 'The Good, The Bad and the Ugly'
print(title.split(' '))
print(title.split(','))
print(title.split(''))
print(title[:6])


fruits = [1, 4, 2, 9, 7, 8, 9, 3, 1]
print(fruits.count(','))


my_string = 'count, the number  of spaces'
print(my_string.count('r'))


welcome_message = 'Hello, World!'
print(welcome_message.replace('Hello', 'Goodbye'))
print(welcome_message.istitle())


welcome = 'Hello {}!'
print(welcome.format('Mars'))

string = '{name} is {age} years old.'
print(string.format(name = 'Adam', age = 20))

print('{:,}'.format(1233565464321))

mix_string = 'Denyse,Marie,Smith,21,London,UK'
print(mix_string.replace(',', ' '))
print(mix_string.find('UK'))


first_string = input('write a word: ')
second_string = input('another word please: ')
new_string = first_string + ' ' + second_string
print(new_string)
print(len(new_string))
print(new_string.upper())
print(new_string.find('bus'))

km = int(input('Please enter distance in Kilometres: '))
mile = km * 0.6214
print('The %d kilometres is equal to %0.2f miles.' %(km, mile))


a=[1,2,3,4]
b=[sum(a[0:x+1]) for x in range(0,len(a))]
print(b)


liste=[“eat”, “tea”, “tan”, “ate”, “nat”, “bat”]
sorted_list=[]
sonuc=[]
for i in liste:
  if sorted(i) not in sorted_list:
    sorted_list.append(sorted(i))
for a in range(len(sorted_list)):
  sonuc.append([i for i in liste if sorted(i)==sorted_list[a]])
print(sonuc)


mylist = ['eat', 'tea', 'tan', 'ate', 'nat',           bat”]
emptylist = []
for i in mylist:
    tempSet = set(i)
    templist = []
    for j in range(len(mylist)):
        if tempSet == tempSet.intersection(set(mylist[j])):
            templist.append(mylist[j])
    if templist not in emptylist:
            emptylist.append(templist)
    templist = []
print(emptylist)




liste = ['eat']
for i in liste:
    print(sorted(i))






 