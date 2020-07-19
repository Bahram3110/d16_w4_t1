numbers = list(range(-10, 10))

def num (x):
    if x < 0:
        return -1
    elif x >=0:
        return 1
    else:
        pass
new_list = map(num, numbers)
print(list(new_list))