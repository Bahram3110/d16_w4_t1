name = input('Введите имя: ')
name1 = name.lower()
name2 = name[::-1]
name2 = name2.lower()


def cheking_name (name_revers):
    if name1 == name2:
        print("True")
    else:
        print('False')

cheking_name(name)