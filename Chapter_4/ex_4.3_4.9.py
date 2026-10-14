# ex.4.3
for numb in range(1, 21):
    print(numb)
print()

# ex.4.4
# for numb in range(1, 1_000_001):
    # print(numb)
# print()

# ex.4.5
million_list = list(range(1, 1_000_001))
print(f'min list = {min(million_list)}, max list = {max(million_list)}')
print(f'sum list = {sum(million_list)}')
print()

# ex.4.6
number_odd_list = list(range(1, 20, 2))
for number in number_odd_list:
    print(number)
print()

# ex.4.7
number_odd_list = list(range(3, 30, 3))
number_odd3_list = []
for number in number_odd_list:
    number_odd3_list.append(number)
print(number_odd3_list)
print()

# ex.4.8
for number in range(1, 11):
    number_cube = number ** 3
    print(number_cube)
print()

# ex.4.9
number_cube_list = [number ** 3 for number in range(0, 11)]
print(number_cube_list)