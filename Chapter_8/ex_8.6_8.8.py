# ex.8.6
# def city_country(city, country):
#     """Return city - country"""
#     message = f'{city} capital of {country}.'
#     return message

# city_country_1 = city_country('Borisoglebsk', 'Russia')
# print(city_country_1)
# city_country_2 = city_country('London', 'England')
# print(city_country_2)
# city_country_3 = city_country('Gondor', 'Middle Earth')
# print(city_country_3)

# ex.8.7
# def make_album(artist, album):
#     """Make album function"""
#     saved_album = {}
#     saved_album[artist] = album
#     return saved_album

# album_1 = make_album('Slipknot', 'Iowa')
# for art, alb in album_1.items():
#     print(f'{art} - {alb}')

# album_2 = make_album('Inflames', 'Clayman')
# for art, alb in album_2.items():
#     print(f'{art} - {alb}')

# album_3 = make_album('Anup Sastry', 'Cristal')
# for art, alb in album_3.items():
#     print(f'{art} - {alb}')

# ex.8.8
def make_album(artist, album):
    """Make album function"""
    saved_album = {}
    saved_album[artist] = album
    return saved_album

while True:
    art = input('Input artist: ')
    alb = input('Input album: ')
    art_alb = make_album(art, alb)
    for art1, alb1 in art_alb.items():
        print(f'{art1} - {alb1}')
    end_responded = input('Are you quit?("q" for quit, other-cont)): ')
    if end_responded == 'q':
        print('Goodbye')
        break
    else:
        continue