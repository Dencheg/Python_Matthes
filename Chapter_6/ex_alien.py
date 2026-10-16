# alien dictionary
aliens_list = []
for alien in range(10):
    new_alien = {'color':'green', 'point':'5', 'speed':'slow'}
    aliens_list.append(new_alien)

for alien in aliens_list[:5]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['point'] = '10'
        alien['speed'] = 'medium'

for alien in aliens_list[:3]:
    if alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['point'] = '15'
        alien['speed'] = 'fast'

for alien in aliens_list:
    print(alien)