numbers = [3, 7, 9, 12, 42]
target = 12

def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

result = linear_search(numbers, target)
print("Index of target:", result)