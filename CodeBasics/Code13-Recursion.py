def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)

def feb(n):
    if n == 0 or n == 1:
        return n
    return feb(n-1) + feb(n-2)

print(sum(10))
print(feb(6))