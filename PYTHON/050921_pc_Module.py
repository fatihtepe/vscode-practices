from random import choice

city = ['Stockholm', 'Istanbul', 'Seul', 'Cape Town']
print(choice(city))  



import random 

city = ['Stockholm', 'Istanbul', 'Seul', 'Cape Town']
print(random.choice(city))  
print(random.random())  # generates random float nubers range of (0, 1)


import string

print(string.punctuation)

print(dir(string))

print(string.digits)



import datetime

print(datetime.date.today())
print(datetime.datetime.now())


from datetime import date

birth = date(571, 4, 22)
death = date(632, 6, 8)

days = date.toordinal(death) - date.toordinal(birth)
print(days)



import random   

city = ['Stockholm', 'Istanbul', 'Seul', 'Cape Town']
print(random.choice(city))
  

vowels = ['a', 'e', 'i', 'o', 'u']
sentence = '@C8113 - Kaan sayenizde el attim :)'
count = 0
for i in sentence:
    if i in vowels:
        count += 1
print(f'Sonuc: {count}')



vowels = ['a', 'e', 'i', 'o', 'u']
sentence = '@C8113 - Kaan sayenizde el attim :)'
count = sum(1 if i in vowels else 0 for i in sentence)
print(f'Sonuc: {count}')

vowels = ['a', 'e', 'i', 'o', 'u']
sentence = 'Kaan hocam sayenizde el attim :)'
print('Sonuc:', len(list(filter(lambda x: x in vowels, sentence ))))


def count_vowels(sentence):
    count = 0
    for i in sentence:
        if i in 'aeiou':
            count += 1
    return count

print('Sonuc:', count_vowels('Baska bir cozum'))


def vowel_counter(text):
    count = 0
    for i in text.lower():
        if i in ["a", "e", "u", "i", "o"]:
            count +=1
    return count

print(vowel_counter("Bu isi basaririm"))

txt = "welcome to the jungle"

x = txt.split()

print(x)


sentence = 'Bu isi basaririm' 
x = sentence.split()
sonuc = len(x[0])
for i in range(1, len(x)):
    if len(x[i]) < sonuc:
        sonuc = len(x[i])
print('Sonuc: ', sonuc)

sentence = 'Bu isi basaririm' 
sonuc = 99
for word in sentence.split():
    if len(word) < sonuc:
        sonuc = len(word)
print('Sonuc: ', sonuc)

sentence = 'Bu isi basaririm' 
print('Sonuc: ', min(len(word) for word in sentence.split()))

sentence = 'Bu isi basaririm' 
print('Sonuc: ', len(min(sentence.split())))


    