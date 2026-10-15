# # ex.5.3
# alien_color = 'green'
# print('V.1')
# if alien_color == 'green':
#     print('You earned 5 points')
# print('V.2')
# if alien_color == 'red':
#     print('You earned 5 points')

# # ex.5.4
# print('V.1')
# alien_color = 'green'
# if alien_color == 'green':
#     print('You earned 5 points')
# else:
#     print('You earned 10 points')
# print('V.2')
# if alien_color == 'red':
#     print('You earned 5 points')
# else:
#     print('You earned 10 points')

# ex.5.4
# print('V.1')
# alien_color = 'green'
# if alien_color == 'green':
#     print('Killed GREEN. You earned 5 points')
# elif alien_color == 'yellow':
#     print('Killed YELLOW. You earned 10 points')
# elif alien_color == 'yellow':
#     print('Killed RED. You earned 15 points')
# print('V.2')
# alien_color = 'yellow'
# if alien_color == 'green':
#     print('Killed GREEN. You earned 5 points')
# elif alien_color == 'yellow':
#     print('Killed YELLOW. You earned 10 points')
# elif alien_color == 'red':
#     print('Killed RED. You earned 15 points')
# print('V.2')
# alien_color = 'red'
# if alien_color == 'green':
#     print('Killed GREEN. You earned 5 points')
# elif alien_color == 'yellow':
#     print('Killed YELLOW. You earned 10 points')
# elif alien_color == 'red':
#     print('Killed RED. You earned 15 points')

# ex.5.6
print('Stage of life.')
age = 99
if age < 2:
    print('This is infant.')
if 2 <= age < 4:
    print('This is toddler.')
if 4 <= age < 13:
    print('This is child.')
if 13 <= age < 20:
    print('This is teenager.')
if 20 <= age < 65:
    print('This is adult.')
if 65 <= age :
    print('This is elderly person.')
print()

# ex.5.7
fruit_list = ['banana', 'strawberry', 'kiwi']
fruit_1, fruit_2, fruit_3 = 'banana', 'orange','strawberry'
fruit_4, fruit_5 = 'pear', 'kiwi'
if fruit_1 in fruit_list:
    print(f"You really lovely {fruit_1}")
else:
    print(f'{fruit_1.title()}. Fruit is not among the favorites')
print('---')
if fruit_2 in fruit_list:
    print(f"You really lovely {fruit_2}")
else:
    print(f'{fruit_2.title()}. Fruit is not among the favorites')
print('---')
if fruit_3 in fruit_list:
    print(f"You really lovely {fruit_3}")
else:
    print(f'{fruit_3.title()}. Fruit is not among the favorites')
print('---')
if fruit_4 in fruit_list:
    print(f"You really lovely {fruit_4}")
else:
    print(f'{fruit_4.title()}. Fruit is not among the favorites')
print('---')
if fruit_5 in fruit_list:
    print(f"You really lovely {fruit_5}")
else:
    print(f'{fruit_5.title()}. Fruit is not among the favorites')
print('---')