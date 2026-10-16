# ex.6.4
print('Glossary list:')
definition_1 = f'a program that translates the entire source code into\n'
definition_1 += f'  machine code all at once before execution, creating a\n'
definition_1 += '  standalone file.'
definition_2 = f'a program that executes code line by line directly at runtime\n'
definition_2 += f'  (like Python does), without prior compilation.'
definition_3 = f'a named storage location (or label) that holds a specific\n'
definition_3 += '  value or piece of data in a program.'
definition_4 = f'a specialized format for organizing, storing, and managing\n'
definition_4 += '  data efficiently (such as lists or dictionaries).'
definition_5 = f'a named block of code designed to perform a specific\n'
definition_5 += '  task that can be reused anywhere in the program.'
definition_6 = f'a step-by-step set of instructions for solving\n'
definition_6 += '  a specific problem.'
definition_7 = f'a control structure that repeats a block of code as\n'
definition_7 += '  long as a specified condition is met.'
definition_8 = f'a data structure that stores a collection of elements of the\n'
definition_8 += '  same type in a specific order.'
definition_9 = f'a feature that performs different actions depending on\n'
definition_9 += '  whether a condition evaluates to true or false.'
definition_10 = f'The process of finding and fixing errors or bugs\n'
definition_10 += f'  in a software program.\n'



glossary_list = {'Compiller': definition_1,
                 'Interpreter': definition_2,
                 'Variable': definition_3,
                 'Data structure':  definition_4,
                 'Function': definition_5,
                 'Algoritm': definition_6,
                 'Loop': definition_7,
                 'Array': definition_8,
                 'Condition statemen': definition_9,
                 'Debugging': definition_10,}

print('Glossary list:')
for definition in glossary_list:
    print(f'- {definition} - {glossary_list[definition]}')

# ex.6.5
rivers_dict = {'Vorona':'Russia',
               'Mississippi':'USA',
               'Ganges':'India'}

river_list = []
country_list = []

for river in rivers_dict.keys():
    river_list.append(river)
for country in rivers_dict.values():
    country_list.append(country)

i = len(river_list)
while i != 0:
    print(f'River {river_list[-i]} flows throught {country_list[-i]}.')
    i -= 1
print()

# ex.6.6
favorite_language = {'Denis':'Python',
                    'Nick':'Basic',
                    'Oleg':'Go',
                    'Alex':'Kotlin',
                    'Ivan':'C',}

peoples_survey = []
for people in favorite_language:
    peoples_survey.append(people)
peoples_survey.insert(2, 'Valentin')
peoples_survey.insert(5, 'Alexandr')

print('Result survey:')
for people in peoples_survey:
    if people in favorite_language:
        print(f'- Favorit {people} language is {favorite_language[people]}.')
    else:
        print(f'- {people}, please to take survey.')
print()