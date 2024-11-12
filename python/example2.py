import random

# 1
age = int(input("22"))
if age >= 18:
    print("You can drive.")
elif age >= 16:
    print("Almost there!")
else:
    print("Too young.")

# 2. 
num = int(input("Enter a number: "))
print("Even" if num % 2 == 0 else "Odd")

# 3. 
score = int(input("(0-100): "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# 4.
num = int (input("Your Number"))
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("Zero")

# 5.
age = int(input("22: "))
student = input("Student? (yes/no): ")
if age < 18 or student == "yes":
    print("Discount")
else:
    print("No discount")

# 6.
for i in range(1, 11):
    print(i)

# 7. 
print("Sum:", sum(range(1, 101)))

# 8.
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num * i)

# 9.
colors = ['red', 'green', 'blue', 'yellow']
for color in colors:
    print(color)

# 10.
count = 10
while count > 0:
    print(count)
    count -= 1
print("Liftoff!")

# 11.
target = random.randint(1, 10)
guess = int(input("1-10:"))
while guess != target:
    guess = int(input("Try again: "))
print("Correct!")

# 12. 
total = 0
while True:
    num = int(input("Enter a number (negative to stop): "))
    if num < 0:
        break
    total += num
print("Total:", total)

# Functions

# 13.
def greet():
    print("Hello!")
greet()

# 14. 
def greet(name):
    print("Hello,", name)
greet("Dan")

# 15.
def square(num):
    return num * num
print("Square of 4:", square(4))

# 16.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print("Factorial of 5:", factorial(5))

# 17.
def find_max(lst):
    return max(lst)
print("Max of [1, 5, 3, 9, 2]:", find_max([1, 5, 3, 9, 2]))

# 18.
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
print("0°C to F:", celsius_to_fahrenheit(0))

# 19.
def is_palindrome(word):
    return word == word[::-1]
print("racecar is a palindrome:", is_palindrome("racecar"))

# 20.
def sum_list(lst):
    return sum(lst)
print("Sum of [10, 20, 30, 40]:", sum_list([10, 20, 30, 40]))

# 21.
def prime (n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i ==0:
            return False
        return True 
    print("ls 7 prime?",)

# 22.
def calculator(a, b, op):
    if op == "add":
        return a + b
    elif op == "subtract":
        return a - b
    elif op == "multiply":
        return a * b
    elif op == "divide":
        return a / b
print("10 + 5 =", calculator(10, 5, "add"))
