# ex.3.10
country_list = ['USA', 'India', 'England', 'Bolivia', 'Norway']
print('Vanila list:')
print(country_list)
print('Sorted function list:')
print(sorted(country_list))
print('Vanila list:')
print(country_list)
print('Sorted function (reverse) list:')
print(sorted(country_list, reverse=True))
print('Vanila list:')
print(country_list)
print('Reverse list:')
country_list.reverse()
print(country_list)
print('Reverse list back:')
country_list.reverse()
print(country_list)
print('Method sort list:')
country_list.sort()
print(country_list)
print('Method sort list (reverse):')
country_list.sort(reverse=True)
print(country_list)
print()

# ex.3.11
invite_list = ['Don Karleone', 'Piter Parker', 'Snusmumrik']
for i in range(0, len(invite_list)):
    print(f'Im invite you to lunch sir.{invite_list[i]}.')
print(f"Number of guests: {len(invite_list)}")
print()

# ex.3.12
river_list = ['Vorona', 'Hoper', 'Don', 'Lovchik']
print(f'In river list {len(river_list)} rivers.')
print('Sorted function (reverse) river list:')
print(sorted(river_list, reverse=True))
print('Vanila list:')
print(river_list)
print('Reverse river list:')
river_list.reverse()
print(river_list)
print('Method sort river list:')
river_list.sort()
print(river_list)