
audience_group = 'kid', 'teen', 'adult'
audience = "teen"
if audience in audience_group:
    if audience == "kid":
        print("it is free to go to cinema")
    elif audience == "teen":
        print("discounted price!")
    else: # audience == "adult":
        print("normal price")
else:
    print("No such audience, stay at your home!")

score = float(input('please enter your exam score: '))

if score >= 90:
    if score >= 95:
        score_letter = 'A+'
    else:
        score_letter = 'A'
elif score >= 80:
    if score >= 85:
        score_letter = 'B+'
    else:
        score_letter = 'B'
else:
    score_letter = 'below B'
print('your degre is :', score_letter)


while 0 :
    print('bir')
print(2)

age = input("Enter your age : ")
while not age.isdigit() :
    print("You entered incorrectly!")
    age = input("Enter your age correctly please : ")
print("Great! You entered valid age :", age)


age = input('Enter your age: ')
while age.isdigit():
    print('your age is:', age)
    break


answer = 11
question = ('Guess a number between 0 to 20: ') 
print("Let's play the guessing game!")

while True:
    guess = int(input(question))
    
    if guess < answer:
        print('little higher')
    elif guess > answer:
        print('little lower')
    else:
        print('You are a MINDREADER!')
        break


answer = 28
question = ('What a two-digit number am I thinking of? ') 
print("Let's play the guessing game!")
while True:
    guess = int(input(question))
    
    if guess < answer:
        print('little higher')
    elif guess > answer:
        print('little lower')
    else:
        print('You are a MINDREADER!')
        break



## THE MOST FREQUENT NUMBER

numbers = [-1, 3 , 7 ,4, 3, 0, 3, 16, 3, 7, 0, 0, 1]

item = max(numbers, key = numbers.count)

print(item)
print(numbers.count(item))


## COMFORTABLE WORDS

left = set('gwertasdfgzxcvb')
right = set('yuiophjklmn')

print(left)
print(right)

word = set('clarusway')
print(word)

leftcheck = bool(word.intersection(left))
rightcheck = bool(word. intersection(right))

print(leftcheck)
print(rightcheck)

print(leftcheck and rightcheck)
