# Exercise 1
total = 0
for i in range(1, 5):
    while True:
        try:
            total += float(input(f"Score for subject {i}: "))
            break
        except ValueError:
            print("Invalid input, please enter a number.")
print("Total score:", total)
if total >= 90:
    grade = "A"
elif total >= 81:
    grade = "B"
elif total >= 60:
    grade = "C"
else:
    grade = "D"
print("Final grade:", grade)


# Exercise 2
ch = input("Enter a character: ")
if len(ch) == 1 and ch in "aeiouAEIOU":
    print(f"'{ch}' is a vowel")
else:
    print(f"'{ch}' is not a vowel")


# Exercise 3
s = input("Enter a string: ").lower()
reversed_s = s[::-1]
if s == reversed_s:
    print("It is a palindrome")
else:
    print("It is not a palindrome")


# Exercise 4
s1 = input("Enter s1: ")
s2 = input("Enter s2: ")
mid = len(s1) // 2
first_half = s1[:mid]
second_half = s1[mid:]
print(first_half + s2 + second_half)


# Exercise 5
text = input("Enter a string: ")
counts = {}
for c in text:
    counts[c] = counts.get(c, 0) + 1
print(counts)
for c, n in counts.items():
    print(f"'{c}' appears {n} time(s)")


# Exercise 6
while True:
    try:
        n = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Invalid input, please enter a whole number.")

if n < 0:
    print("Factorial does not exist for negative numbers")
elif n == 0:
    print("The factorial of 0 is 1")
else:
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(f"The factorial of {n} is {result}")


# Exercise 7
while True:
    try:
        n = int(input("Enter a natural number n: "))
        break
    except ValueError:
        print("Invalid input, please enter a whole number.")

total = 0
for i in range(1, n + 1):
    total += i ** 2
print(f"Sum of squares of the first {n} natural numbers: {total}")


# Exercise 8
while True:
    try:
        num = int(input("Enter a positive integer: "))
        break
    except ValueError:
        print("Invalid input, please enter a whole number.")

total = 0
for i in range(1, num + 1):
    total += i
print(f"Sum from 1 to {num}: {total}")


# Exercise 9
numbers = [1, 2, 3, 4, 5]
squared = []
for x in numbers:
    squared.append(x ** 2)
print("Original:", numbers)
print("Squared:", squared)


# Exercise 10
numbers = [1, 2, 3, 4, 5]
squared = [x ** 2 for x in numbers]
print("Original:", numbers)
print("Squared:", squared)


# Exercise 11
lst = [10, 20, 30, 20, 40, 20, 50]
for x in lst[:]:  # loop over a copy so removing is safe
    if x == 20:
        lst.remove(x)
print(lst)


# Exercise 12
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = (7, 8, 9)
result = tuple(a + b + c for a, b, c in zip(tuple1, tuple2, tuple3))
print(result)


# Exercise 13
keys = ["name", "age", "city"]
values = ["Leno", 21, "Giza"]
d = dict(zip(keys, values))
print(d)


# Exercise 14
squares = {k: k ** 2 for k in range(1, 16)}
print(squares)


# Exercise 15
data = {"a": 100, "b": 200, "c": 300}
if 200 in data.values():
    print("200 is found in the dictionary values")
else:
    print("200 is not found in the dictionary values")