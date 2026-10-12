# ex.2.3
name = "Gendalf"
print(f"Hello {name}, are you want learning 'Python' today?")

# ex.2.4
name = "luke"
print(f"Hello {name.lower()}, are you want learning 'Python' today")
print(f"Hello {name.upper()}, are you want learning 'Python' today")
print(f"Hello {name.title()}, are you want learning 'Python' today")

# ex.2.5
print(f'Jaison Statham said:\n\t"Remember - only one error and you errored"')

# ex.2.6
famous_person = 'Jaison Statham'
message = '"Remember - only one error and you errored"'
print(f'{famous_person} said:\n\t{message}')

# ex.2.7
name = "Jaison "
surname = " Statham "
print(f'{name}{surname}-\n\{name.rstrip()}{surname.strip()}-')
print(f'\t{name.rstrip()}{surname.lstrip()}-')

# ex.2.8
name = 'read_me.txt'
print(name.removesuffix('.txt'))