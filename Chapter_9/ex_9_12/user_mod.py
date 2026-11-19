# ex.9.11
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