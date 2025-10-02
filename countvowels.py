s = input("Enter a string: ").lower()
count = sum(1 for c in s if c in "aeiou")
print("Number of vowels =", count)
