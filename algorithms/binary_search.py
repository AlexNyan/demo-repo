#take a list as a parameter
def binary_search(list, item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = int((low+ high)/2)
        guess = list[mid]
        if item == guess :
            return mid
        elif guess > item:
            high = mid -1
        else:
            low = mid + 1
my_list = [1, 2, 3, 5]
print(binary_search(my_list,3))
