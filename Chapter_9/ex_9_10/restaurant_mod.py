# ex.9.9
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

