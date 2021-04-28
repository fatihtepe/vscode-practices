# print('hello world')

# listem = []
# for i in range(5):
#     listem.append(i **2)
# print(listem)

# print([i ** 2 for i in range(5)])



# listem = []
# for i in range(10):
#     if i % 2:
#         listem.append(i ** 2)
# print(listem)

# print([i ** 2 for i in range (10) if i % 2])



# total_odd_num = 0
# total_even_num = 0
# my_list = [12, 3, 4, 556, 767, 8, 88, 99, 4 ,3, 5 ,7 ,79]
# for i in my_list:
#     if i % 2:
#         total_odd_num += 1
#     else:
#         total_even_num += 1
        
# print(total_odd_num)
# print(total_even_num)



# for i in range (1, 10):
#     print(str(i) * i)




# total = 0
# for i in range(1, 75):
#     total += i
# print(total)

# print(sum(i for i in range(1, 75)))
    
    
    
# numList = ['1', '2', '3', '4']
# print(', '.join(numList))
    

# times = int(input('How many times you want?: ')) 
# for i in range(times):
#     print('You are learning python!')



# number = int(input('Enter a number between 1-10: '))

# for i in range(11):
#     print(f'{number} X {i} = {number * i}')



# n = int(input('Enter a Number: ').strip())
# if n % 2 == 1:
#     print('Weird')
# elif n % 2 == 0 and (n>=2 and n<5):
#     print('Not Weird')
# elif n % 2 == 0 and (n>= 6 and n<20):
#     print('Weird')
# elif n % 2 == 0 and n > 20:
#     print('Not Weird')


# seq = range(5)
# print(*seq)
# print(list(seq))

# print(seq.split(','))


# print(*'separate')
# print(list(range(11)))
# print(tuple(range(11)))
# print(*range(1, 25, 2))
# print(*range(11, 2, -2))



# sentence = input('Please write whatever you want!')
# words = sentence.split()
# i = 0
# longest = 0

# while i < len(words):
#     if len(words[i]) > longest:
#         longest = len(words[i])
#     i += 1
# print(f'length of longest word is {longest}')



# eleman = 'ahmet -, clarusway[]'
# for i in eleman:
#     print(i, end='+')

# word = 'Clarusway'
# count = 0
# for i in word:
#     count += 1
#     if count < len(word):
#         i += '-'
#     print(i, end='')


# name = 'fatihtepe'

# count = 0

# for i in name:
#     count += 1
#     if count < len(name):
#         i += ','
#     print(i, end='')


# names = {'name': 'Fatih', 'age': 24, 'school': 'SpaldingU'}
# names['name'] = 'Sami'
# print(names['name'])

# # for i, b in names.items():
# #     print(i,':', b)

# # for i in names.values():
# #     print(i)

# count = 0
# print('Starting..')
# while count < 10:
#     print(count, ' ', end='')
#     count += 1
# print()
# print('Done')       



# import random

# roll = 'y'
# while roll == 'y':
#     print('Rolling the dices...')
#     print('The values are...')
#     dice1 = random.randint(1, 6)
#     print(dice1)
#     dice2 = random.randint(1, 6)
#     print(dice2)
#     roll = input('roll the dices again? (y / n): ')



   
