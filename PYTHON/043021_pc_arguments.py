# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.")
#     print("-- Lovely plumage, the", type)
#     print("-- It's", state, "!")


# parrot(1000)                                          # 1 positional argument
# parrot(voltage=1000)                                  # 1 keyword argument
# parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
# parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments 
# parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
# parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword



# def city(capital, continent='Europe'):
#     print(capital, 'in', continent)

# city('Athens')  # we don't have to pass any arguments into 'continent'
# city('Ulaanbaatar', continent='Asia')  # we can change the default value by kwargs
# city('Cape Town', 'Africa')  # we can change the default value by positional args.


# def fruiterer(fruit1, fruit2) :
#     print('I want to get', fruit1, 'and', fruit2)
        
# fruiterer('orange', 'banana')


# def fruiterer(*fruit) :
#     print('I want to get :')
#     for i in fruit :
#         print('-', i)
        
# fruiterer('orange', 'banana', 'melon', 'ananas', 'apple')


# def animals(**kwargs):
#     for key, value in kwargs.items():
#         print(value, "are", key)
 
# animals(Carnivores="Lions", Omnivores="Bears", Herbivores="Deers", Nomnivores="Human")



# def gene(x, y):  # defined by positional args
#     print(x, "belongs to Generation X")
#     print(y, "belongs to Generation Y")
  
# gene('John', 'Amy')
# dict_gene = {'y' : "Marry", 'x' : "Fred"}
# gene(**dict_gene)  # we call the function by a single argument(variable)



# def gene(x='Solomon', y='David'):  # defined by kwargs (default values assigned to x and y)
#     print(x, "belongs to Generation X")
#     print(y, "belongs to Generation Y")
 
# dict_gene = {'y' : "Marry", 'x' : "Fred"}
# gene(**dict_gene) 
# gene()


# def printSuccess():
#     '''You can make explanation about function'''
#     print('I am done')
#     print('send me another task')
    
# printSuccess()

# print(printSuccess.__doc__)  # you call __doc__



# def printMessage(msg):
#     print(msg)

# printMessage('Be warrior not a worrior!')


# def printMsg(msg):
#     '''The function prints the message supplied by the user
#     or prints that msg is not in the form of string'''
#     if isinstance(msg, str):
#         print(msg)
#     else:
#         print('Your input argument is not a string')
#         print('Here is the type of what you have supplied')

# printMsg('Be a warrior not a worrier!!')



# def mypow(a, b):
#     '''this function computes power just like builtin pow functtion'''
#     c = a**b
#     print(c)
  
# mypow(3,4)



# def checkArgs(a, b, c):
#     if isinstance(a, (int, float)) and (b, (int, float)) and (a, (int, float)):
#         print((a+b+c)**2)
#     else:
#         print('error: the input arguments are not of the expected types')

# checkArgs(5, 6, 8)


# def get_initial(name):
#     initial = name[0:1].upper()
#     return initial

# first_name = input('enter your first name: ')
# first_name_initial = get_initial(first_name)

# print(first_name_initial)



# def team_names(*teams) :
#     print('The teams in Premier League are :')
#     for i in teams :
#         print('-', i)

# team_names('Liverpool', 'M.United', 'M.City', 'Arsenal')


# def make_sentence(**kwargs):
#     result = ""
#     # Iterating over the Python kwargs dictionary
#     for i in kwargs.values():
#         result += i
#     return result

# print(make_sentence(a="I ", b="love ", c="Clarusway!"))



# def team_league(team, league='Premier League'):
#     print(team, 'in', league)

# team_league('Liverpool')


# def my_function(first, last) : 
#     print('Your first name is :', first)
#     print('Your last name is :', last)

# my_function('Richard', 'Rice') 



# def team_names(*teams) :
#     print('The teams in Premier League are :')
#     for i in teams :
#         print('-', i)

# teams = ('Liverpool', 'M.United', 'M.City', 'Arsenal')

# team_names(*teams)



# i = 200

# while i >=151:
#     i -= 2
#     print(i)
    