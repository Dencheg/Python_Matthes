# ex.9.4
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
        self.number_served = 0

    def open_restauraunt(self):
        """display a message that the open a restaurant"""
        print(f'!!!"{self.restaurant_name}" is OPEN!!!')

    def discribe_restaurant(self):
        """indicates a type of cuisine and  name of restaurant"""
        print(f'Us restaurant "{self.restaurant_name.upper()}"')
        print(f'THE BEST restaurant {self.cuisine_type} cuisine!')

    def displayed_number_served(self):
        """displayed number served clients"""
        text = f'Number of served clients: {self.number_served}'
        return text

    def change_number_served(self, number):
        """changed number served clients"""
        if number <= self.number_served :
           text = 'You cannot decreace the number of clients'
           text += 'or specify the same number.'
        else:
            self.number_served = number
            text = 'The number of clients is changed.'
        return text
    
    def increment_number_served(self, in_number):
        """increament number served clients"""
        if in_number + self.number_served <= self.number_served :
           text = 'You cannot decreace the number of clients.'
        else:
            self.number_served += in_number
            text = 'The number of clients is changed.'
        return text

# restaurant_1 = Restaurant('Crazy Ivan', 'Russian')
# print(f'"{restaurant_1.restaurant_name}", "{restaurant_1.cuisine_type}"')
# Changed the numbers of served clients###############
# print(f'Number of served {restaurant_1.number_served}')
# restaurant_1.number_served = 15
# print(f'Number of served {restaurant_1.number_served}')
#######################################################
# restaurant_1.open_restauraunt()
# restaurant_1.discribe_restaurant()
# Changed the numbers of served clients with method#####
# print(restaurant_1.displayed_number_served())
# print(restaurant_1.change_number_served(15))
# print(restaurant_1.displayed_number_served())
# print(restaurant_1.change_number_served(7))
# print(restaurant_1.displayed_number_served())
#######################################################
# Increment the numbers of served clients with method##
# print(restaurant_1.increment_number_served(3))
# print(restaurant_1.displayed_number_served())
# print(restaurant_1.increment_number_served(3))
# print(restaurant_1.displayed_number_served())
# print(restaurant_1.increment_number_served(-3))
# print(restaurant_1.increment_number_served(3))
# print(restaurant_1.displayed_number_served())
#######################################################


# ex.9.5
class User():
    """user profil with a summari information"""

    def __init__(self, first_name, last_name, age='', level=''):
        """initializes attributes of user"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.level = level
        self.login_attemps = 0

    def increment_login_attemps(self):
        """increment of number of login attemps for user"""
        self.login_attemps += 1
        print('|||Login attemp recorded|||')

    def greet_user(self):
        """displays a personal greeting for user"""
        self.increment_login_attemps()
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

    def number_login_attemps(self):
        """displayed number login attemps for user"""
        text = f'Number of login atteps: {self.login_attemps}'
        return text

    def reset_login_attemps(self):
        """reset login attemps for user"""
        self.login_attemps = 0
        print(f'Login attemps is reset ({self.login_attemps})')
                     
user_1 = User('Galaktion', 'Fildiperstov', '35', '5')
user_1.greet_user()
print(user_1.number_login_attemps())
user_1.discribe_user()
user_1.greet_user()
print(user_1.number_login_attemps())
user_1.greet_user()
print(user_1.number_login_attemps())
user_1.reset_login_attemps()
print()

user_5 = User('Mario', 'Plumber', '35', '3')
user_5.greet_user()
print(user_5.number_login_attemps())
user_5.discribe_user()
user_5.greet_user()
print(user_5.number_login_attemps())
user_5.reset_login_attemps()
print()


user_0 = User('admin', 'admin')
user_0.greet_user()
user_0.discribe_user()
print(user_0.number_login_attemps())
user_0.reset_login_attemps()