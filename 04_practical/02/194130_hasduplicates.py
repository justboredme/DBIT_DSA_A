numbers = [3, 7, 9, 12, 42, 7]

def has_duplicates(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return True
    return False

result = has_duplicates(numbers)
print("Contains duplicates:", result)