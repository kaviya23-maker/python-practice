def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

a, b = map(int, input("Enter two numbers: ").split())
print("GCD =", gcd(a, b))
