numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(max)



matrix =[[1, 2, 3, 4],[4, 5, 6, 7], [8, 9, 10]]
    
for l in matrix:
    for i in l:
        print(i, end=', ')



user_permission = {'read', 'write', 'exute'}
new_user_permission = {'write'}

print(new_user_permission.difference(user_permission))

print(user_permission.difference(new_user_permission))

import calendar

print(calendar.monthrange(2021, 2))
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
offset = 2
for day in range(1, 29):
    print(day, weekdays[(day+offset-1) % 7])


import calendar
print(calendar.isleap(2021))  # False
print(calendar.isleap(2024))  # True


mylist = ['a', 'b', 'd', 'c', 'g', 'e']
for i, item in enumerate(mylist):
    print(i, item)
 
 
y = []
for i in enumerate(mylist):
    y.append(i)
print(y)

print('-'.join(mylist))


    
OPEN = 1
IN_PROGRESS = 2
CLOSED = 3
def handle_open_status():
    print('Handling open status')
def handle_in_progress_status():
    print('Handling in progress status')
def handle_closed_status():
    print('Handling closed status')
def handle_status_change(status):
    if status == OPEN:
        handle_open_status()
    elif status == IN_PROGRESS:
        handle_in_progress_status()
    elif status == CLOSED:
        handle_closed_status()
handle_status_change(1)  # Handling open status
handle_status_change(2)  # Handling in progress status
handle_status_change(3)  # Handling closed status


new_list = [x for x in range(10)] #list comprehension
print(new_list)
# output => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

new_dict = {x:x+1 for x in range(10)} #dictionary comprehension
print(new_dict)
# output => {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10}

new_set = {x for x in range(10)} #set comprehension
print(new_set)
# output => {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

new_gen = (x for x in range(10)) #generator comprehension
print(new_gen)
# output => <generator object <genexpr> at 0x10556e6d0>



def is_palindrome(str):
      return str == str[::-1]

print(is_palindrome('hannah'))



my_list = [0,1,2,3,6,7,9,11]

result = filter(lambda x: x % 2!=0, my_list)

print(list(result))




echo_word = lambda x, y: x * y
print(echo_word('hello', 3))


