i = 0
while i <= 5:
    print(i)
    i += 1
print('Done')



def sum_double(x, y) :
    return x + y if x != y else (x + y) * 2

print(sum_double(2, 2))



from functools import reduce 
double = (2, 2)

print(reduce(lambda x, y : (x + y) if x != y else \
    (x + y) * 2, double))


def not_string(word):
    return word if word.startswith("not") else "not " + word

print(not_string('not bad'))


from datetime import datetime
print(datetime.now())

for x in range(0, 10):
    if x % 2:
        print('odd number', x)
    else:
        print('even number', x)
        


odd_number = [list(filter(lambda x: x % 2 != 0, range(0, 10)))]
print(odd_number)
print(list(filter(lambda x: x % 2 == 0, range(0, 10))))


from collections import Counter

print(Counter('google'))




def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

print(char_frequency('google.com'))


sentence = input('Please enter a word or sentece: ')
new = sentence.lower()

for i in range(len(sentence)):
    b = t.count(new[i])
    print("{} -- {}".format(sentence[i], b))
    
    

sentence = input('Please enter a word or sentece: ').lower()

for i in range(len(sentence)):
    value = sentence.count(sentence[i])
    print("{} -- {}".format(sentence[i], value))




    
sentence = input('Please enter: ')

def sentence_dict(sentence):
    s_dict = {}
    for char in sentence:
        if char in s_dict.keys():
            s_dict[char] += 1
        else:
            s_dict[char] = 1
    return s_dict

print(sentence_dict(sentence))


def string_dict_v2(sentence):
    d = {}
    for char in sentence:
        d[char] = d.get(char, 0) + 1
    return d

print(string_dict_v2(sentence))

        
def front_back(word):
    if len(word) == 1:
        return word
    return word[-1] + word[1:-1] + word[0]




def my_min(*args):
    return min(args)





def my_min(*args):
    m = 9999999
    
    for i in args:
        if i < m:
            m = i
    return m 




def missing_char(word, n):
    return word[:n] + word[n+1:]

print(missing_char('armut', 2))