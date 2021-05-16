audience_group = 'kid', 'teen', 'adult'
audience = 'handsome'
if audience in audience_group:
    if audience == 'kid':
        print('it is free to go to cinema')
    elif audience == 'teen':
        print('discounted price!')
    else: 
        print('normal price')
else:
    print('No such audience, stay at your home!')


score = int(input('Enter your score: '))
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

print('Your degree %s' % score_letter)


country = input('What counry do you live in? ')
tax = 0
if country.lower() == 'canada':
    province = input('What province do you live in? ')
    if province.title() in ('Alberta', 'Yukon', 'Nunavut'):
        tax = 0.05
    elif province.title() == 'Ontario':
        tax = 0.13
    else:
        tax = 0.15
else:
    tax = 0.0
print(tax)


# A student makes honour roll if their average is >=85
# and their lowest grade is not below 70
gpa = float(input('What was your Grade Point Average? '))
lowest_grade = float(input('What was your lowest grade? '))

# if gpa >= .85 and lowest_grade >= .70:
#         print('You made the honour roll')


if gpa >= .85 and lowest_grade >= .70:
    honour_roll = True
else:
    honour_roll = False

# Somewhere later in your code if you need to check if students is 
# on honour roll, all I need to do is check the boolean variable
# I set earlier in my code
if honour_roll:
    print('You made honour roll')
else:
    print('Believe in yourself! Next time!')
    

if gpa >= .85 and lowest_grade >= .70:
    honour_roll = True
else:
    honour_roll = False
