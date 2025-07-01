numbers= [3,7,9,12,42]

def sum_of_elements(list):
    total = 0
    for num in list:
        total += num
    return total

print(sum_of_elements(numbers))