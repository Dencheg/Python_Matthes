# ex.9.1
class Restaurant():
    """
    description of restaurant and its cuisine
    """
    def __init__(self, restaurant_name, cuisine_type):
        """
        initializes attributes of restaurant
        and its cuisine
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def open_restauraunt(self):
        """display a message that the open a restaurant"""
        print(f'!!!"{self.restaurant_name}" is OPEN!!!')


    def discribe_restaurant(self):
        """indicates a type of cuisine and  name of restaurant"""
        print(f'Us restaurant "{self.restaurant_name.upper()}"')
        print(f'THE BEST restaurant {self.cuisine_type} cuisine!')

# restaurant_1 = Restaurant('Crazy Ivan', 'Russian')
# print(f'"{restaurant_1.restaurant_name}", "{restaurant_1.cuisine_type}"')
# restaurant_1.open_restauraunt()
# restaurant_1.discribe_restaurant()
# print()

# ex.9.2
# restaurant_2 = Restaurant('Cunning Uncle Lao', 'Chinese')
# restaurant_2.discribe_restaurant()
# print()
# restaurant_3 = Restaurant('Monsieur Froggy', 'French')
# restaurant_3.discribe_restaurant()
# print()
# restaurant_4 = Restaurant('Fat Margaret', 'American')
# restaurant_4.discribe_restaurant()
# print()

# ex.9.3
class User():
    """user profil with a summari information"""

    def __init__(self, first_name, last_name, age='', level=''):
        """initializes attributes of user"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.level = level

    def greet_user(self):
        """displays a personal greeting for user"""
        if self.first_name == 'admin' and self.last_name == 'admin':
            print('Wellcome back mr. Neo *||||')
            print('v^v^v^v^v^v^v^v^v^v^v^v^v^')
        else:
            print(f'Hello {self.first_name}!')

    def discribe_user(self):
        """discribe summary information of user"""
        print('User information:')
        print(f'- name: {self.first_name}\n- surname: {self.last_name}')
        if self.age != '' and self.age != '':
            print(f'- age: {self.age}\n- level: {self.level}')
            lev = int(self.level)
            if lev == 5:
                print(' /\\ ')
                print('<:)>')
                print(' vv ')
            else:
                pass
        else:
            pass
        print()
            
user_1 = User('Galaktion', 'Fildiperstov', '35', '5')
user_1.greet_user()
user_1.discribe_user()

user_5 = User('Mario', 'Plumber', '35', '3')
user_5.greet_user()
user_5.discribe_user()

user_0 = User('admin', 'admin')
user_0.greet_user()
user_0.discribe_user()

