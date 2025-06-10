def head_recursion(n):
    if n < 0:
        return 0
    head_recursion(n - 1)
    print(f"{n} Head recursion")
    return None

head_recursion(7)