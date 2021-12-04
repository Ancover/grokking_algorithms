def binary_search(list, item):
    low = 0 # the lowest value of list (first element of list)
    high = len(list) - 1 # the highest value of list (last element of list)

    while low <= high:
        mid = int((high + low)/2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1  # if the number we are looking for is less than mid, we can throw away numbers, that are bigger than mid
        else:
            low = mid + 1 # if the number we are looking for is bigger than mid, we can throw away numbers, that are less than mid
    return None

list = [12, 11, 4, 123, 41, 13, 22, 35]
list = sorted(list) # binary search works only with sorted arrays
print(binary_search(list, 35))