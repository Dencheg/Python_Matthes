# ex.8.3
def make_shirt(size, text):
    """Make shirt with size and text"""
    print(f'Ok, we make shirt with size: {size} and text:')
    print(f'\t"{text}"')

make_shirt('M', 'I love Futurtama')
make_shirt(text='I love Simpsons', size='XL')

# ex.8.4
def make_shirt(size='L', text='I love Python'):
    """Make shirt with size and text rev.1"""
    print(f'Ok, we make shirt with size: {size} and text:')
    print(f'\t"{text}"')

make_shirt()
make_shirt(text='I love Rust', size='S')

# ex.8.5
def discribe_city(city, country='France'):
    """City in country"""
    print(f'{city} is in {country}')

discribe_city('Paris')
discribe_city('London', country='France')
discribe_city('New York', 'USA')
