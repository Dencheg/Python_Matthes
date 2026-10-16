# ex.6.1
famous_person = {'first_name':'Frodo',
                 'surname':'Baggins',
                 'city':'Shir',
                 'age':'50'}
print('Famous person:')
print(f'First name: {famous_person['first_name']}')
print(f'Surname: {famous_person['surname']}')
print(f'City: {famous_person['city']}')
print(f'Age: {famous_person['age']}\n')

# ex.6.2
favorite_numbers = {'Denis':'42',
                    'Nick':'15',
                    'Oleg':'88',
                    'Alex':'45',
                    'Ivan':'27',}

print('Favorite numbers:')
print(f'- Denis: {favorite_numbers['Denis']}')
print(f'- Nick: {favorite_numbers['Nick']}')
print(f'- Oleg: {favorite_numbers['Oleg']}')
print(f'- Alex: {favorite_numbers['Alex']}')
print(f'- Ivan: {favorite_numbers['Ivan']}\n')

# ex.6.3
definition_1 = 'a program that translates the entire source code into '
definition_1 += 'machine code all at once before execution, creating a '
definition_1 += 'standalone file.'
definition_2 = 'a program that executes code line by line directly at runtime'
definition_2 += ' (like Python does), without prior compilation.'
definition_3 = 'a named storage location (or label) that holds a specific '
definition_3 += 'value or piece of data in a program.'
definition_4 = 'a specialized format for organizing, storing, and managing '
definition_4 += 'data efficiently (such as lists or dictionaries).'
definition_5 = 'a named block of code designed to perform a specific '
definition_5 += 'task that can be reused anywhere in the program.'

glossary_list = {'Compiller': definition_1,
                 'Interpreter': definition_2,
                 'Variable': definition_3,
                 'Data structure':  definition_4,
                 'Function': definition_5}

print('Glossary list:')
print(f'- Compiller - {glossary_list['Compiller']}')
print(f'- Interpreter - {glossary_list['Interpreter']}')
print(f'- Variable - {glossary_list['Variable']}')
print(f'- Data structure - {glossary_list['Data structure']}')
print(f'- Function - {glossary_list['Function']}\n')