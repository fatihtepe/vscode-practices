answer = 88
print('Let\'s play a game! Guess the number in my mind!')

while True:
    guess = int(input('make a guess!: '))
    if guess > answer:
        print('little lower')
    elif guess < answer:
        print('little higher')
    else:
        print('Good for you!')
        break

flowers = ['Rose', 'Orchid', 'Tulip']
newlist = 0
x = len(flowers)

while x > 0:
    print(flowers[newlist])
    x-= 1
    newlist += 1

numbers = [12, 37, 5, 42, 8, 3]
odd = []
even = []

while len(numbers) > 0:
    i = numbers.pop()
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(odd)
print(even)

n = int(input('enter a number between 1-10: '))

for i in range(11):
    print('{} X {} = '.format(n, i), n*i)



