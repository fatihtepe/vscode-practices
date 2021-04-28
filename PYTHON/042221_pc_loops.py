for somethingvalid in [1, 2, 3, 4, 5]:
    print(somethingvalid)
    
    
seasons = ("spring", "summer", 'autumn', 'winter')
for michaeladams in seasons:
    print("the season in row is: ", michaeladams)
    print("this line will be written how many times?")
    print("333333333333333333?")



names = ["Ahmed", "Aisha", "Adam", "Joseph", "Gabriel"]
for name in names:
    print("hello", name)
    print("hello {}".format(name))
    print(f"hello {name}")



our_list = []
for i in range(1, 6):
    our_list.append(i)
    print("i: ", i, "our list: ", our_list)
    if i == 3:
        break
print("------------------")
print(our_list)



course = 'clarusway'
say = 0
for i in course:
    say += 1
    if say < len(course):
        i += '-'
    print(i, end='')



user_input = input("please enter a word: ")
counter = 0
for char in user_input:
    counter += 1
    print("counter: ", counter, "length of user input: ", len(user_input))
    if counter >= len(user_input):
        print(char)
print()


number = int(input("please enter a number - between 1 -10 - : "))
print("user input: ", number)
for i in range(number):
    print(number, " X ", i, " = ", number*i)


sentence = input('Plese enter a sentence: ')
longest = 0
i = 0
word_list = sentence.split()
print(word_list)

while i < len(word_list):
    if len(word_list[i]) > longest:
        longest = len(word_list[i])
    i += 1
print('the length of longest word is', longest)
       
       
dict = {
    'meyve1': 'elma',
    'meyve2': 'portakal'
    }

for value in dict.values():
    print(value)

for key, value in dict.items():
    print(key, ':', value)


tell_your_love = int(input('How many times should I say "I love you": '))

for i in range(tell_your_love):
   print('I love you')
            
names = ["Ahmed", "Aisha", "Adam", "Joseph", "Gabriel"]
s= ', '
print(s.join(names))

print('Please enter Yes or No')
age = input('Are you a cigarette addict older than 75 years old?: ').lower().strip() == 'yes'
chronic = input('Do you have a severe chronic disease?: ').lower().strip() == 'yes'
immune = input('Is your immune system too weak?: ').lower().strip() == 'yes'

if chronic and (age or immune):
    print('You are in risky group')
else:
    print('You are not in risky group')

left = set('gwertasdfgzxcvb')
right = set('yuiophjklmn')

word = set('world')

leftcheck = bool(word.intersection(left))
rightcheck = bool(word. intersection(right))

print(leftcheck and rightcheck)