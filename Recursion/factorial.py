def factorial(n):
    assert n >= 0 and int(n) == n, "The number must be a positive integer !!"
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

# def factorial(n):
#     assert n >= 0 and int(n) == n, "The number must be a positive integer !!"
#     if n in [0, 1]:
#         return 1
#     for x in range(1, n):
#         n = x * n 
#     return n

# print(fac(5))
        