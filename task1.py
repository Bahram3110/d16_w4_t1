list1 = range(-15, 15)
def number_1 (n):
    return n % 2 == 0 

def number_2 (n):
    return n % 2 != 0


list_result1 = filter(number_1, list1)
list_result2 = filter(number_2, list1)
list_result1 = list(list_result1)
list_result2 = list(list_result2)
print(len(list_result1))
print(len(list_result2))