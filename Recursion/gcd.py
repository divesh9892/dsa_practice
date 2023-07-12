def gcd(a, b):
    assert int(a) ==a and int(b) == b, "The numbers must be an integer"
    if a < 0:
        a = a * -1
    if a < 0:
        a = a * -1
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

print(gcd(10, 5))