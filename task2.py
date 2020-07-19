nums = range(-12, 12)
nums = list(nums)


def num_sort_x (x):
    return x >= 0

def num_sort_y (y):
    return y < 0

nums_res1 = filter(num_sort_x, nums)
nums_res2 = filter(num_sort_y, nums)
print(list(nums_res1))
print(list(nums_res2))