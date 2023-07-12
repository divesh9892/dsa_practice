def sum_of_digits(n):
    assert n >= 0 and int(n) == n, "The number must be a positive integer !!"
    if n < 10:
        return n
    else:
        return sum_of_digits(n//10) + sum_of_digits(n%10)

print(sum_of_digits(15))


# Alternate
def sum_of_digits_alternate(n):
    assert n >= 0 and int(n) == n, "The number must be a positive integer !!"
    if n == 0:
        return n
    else:
        return n%10 + sum_of_digits(n//10)

print(sum_of_digits_alternate(25))