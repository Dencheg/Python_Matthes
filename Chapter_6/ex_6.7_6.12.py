# ex.6.7
famous_person_1 = {'First name':'Frodo',
                 'Surname':'Baggins',
                 'City':'Shir',
                 'Age':'50'}

famous_person_2 = {'First name':'Tony',
                 'Surname':'Stark',
                 'City':'New-York',
                 'Age':'38'}

famous_person_3 = {'First name':'Neznayka',
                 'Surname':'Nosov',
                 'City':'Sun-City',
                 'Age':'11'}

famous_list = [famous_person_1, famous_person_2, famous_person_3]

i = 0
for famous_person in famous_list:
    i+=1
    print(f'Famous person {i}:')
    for key in famous_person:
        print(f'- {key} is {famous_person[key]}')
    print()

# ex.6.8
Pikachu = {'Owner name':'Ash',
           'Type of animal': 'pokemon'}

Duppi = {'Owner name':'Luke',
        'Type of animal': 'rankor'}

pets = [Pikachu, Duppi]

for  pet_name in pets:
    for key, value in pet_name.items():
        print(f'{key} is {value}.')
    print()
        
# ex.6.9
famous_person_1 = {'First name':'Frodo',
                 'Surname':'Baggins',
                 'City':'Shir',
                 'Age':'50',
                 'Favorite places':['Shir', 'Bree', 'Rivirdale']}

famous_person_2 = {'First name':'Tony',
                 'Surname':'Stark',
                 'City':'New-York',
                 'Age':'38',
                 'Favorite places':'Macdonalds'}

famous_person_3 = {'First name':'Neznayka',
                 'Surname':'Nosov',
                 'City':'Little-City',
                 'Age':'11',
                 'Favorite places':['Moon', 'Sun-City']}

famous_list = [famous_person_1, famous_person_2, famous_person_3]

for i, famous_person in enumerate(famous_list, start=1):
    print(f'Famous person {i}:')
    for key, values in famous_person.items():
            text = ''
            if isinstance(values, list):
                for i, value in enumerate(values, start=1):
                    if i < len(values):
                        text += f'{value} and '
                    elif i == len(values):
                        text += f'{value}'
                print(f'- {key} is {text}')
            else:
                print(f'- {key} is {values}')
    print() 

# ex.6.10
favorite_numbers = {'Denis':['7' ,'12', '42'],
                    'Nick':['9', '15'],
                    'Oleg':['77', '88'],
                    'Alex':['33', '45'],
                    'Ivan':['17', '27']}

print('Favorite numbers:')
for name, numbers in favorite_numbers.items():
    text = ''
    for i, number in enumerate(numbers, start=1):
        if i < len(numbers):
            text += f'{number}, '
        if i == len(numbers):
            text += f'{number}'
    print(f'- {name}: {text}')
print()

# ex.6.11
fact_1 = f"Minas-Tirith astablished of the site \nan another fortress.\n"
fact_2 = f'Vivek divided into two parts of the \nworld.\n'
fact_3 = f'all planet, on continuous city.\n'

cities = {'Minas-Tirith':{'country':'Gondor;',
                        'population':'50 thousand people;',
                        'intrsting fact':fact_1},
                        'Vivek':{'country':'Vvanderfell;',
                        'population':'55 thousand people;',
                         'intrsting fact':fact_2},
                        'Coruscant':{'country':'Galctian Republic;',
                        'population':'1,9 trillion peoples;',
                        'intrsting fact':fact_3}}

for city in cities:
    print(f'Facts abaut city {city}:')
    for fact in cities[city]:
        print(f'- {fact}: {cities[city][fact]}')

# ex.6.12