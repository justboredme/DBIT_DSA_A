numbers = [3, 7, 9, 12, 42]

def find_max(lst):
    if not lst:
        return None
    max_value = lst[0]
    for num in lst[1:]:
        if num > max_value:
            max_value = num
    return max_value

result = find_max(numbers)
print("The largest number is:", result)