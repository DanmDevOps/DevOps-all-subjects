#variables

#1
age = 22
name = "Dan monticciolo"
print(age)
print (name)

#2
x = 10
y = 5
sum = x + y
print(sum)
print(x - y)
print(x * y)
print(x / y)

#3
a = 3
b = 7

a, b = b, a

print(a, b)

#4
length = 10
width = 5
area = length * width
print(area)


#5
greeting = 'Hello, world!'
print("Length:", len(greeting))
print("First character:", greeting[0])
print("Last character:", greeting[-1])


#strings
#6
first_name = "Dan"
last_name = "Monticciolo"
full_name = first_name + " " + last_name
print(full_name)

#7
print(f"My name is {name} and I am {age} years old")

#8
quote = "To be or not to be, that is the question."
print(quote.upper())
print(quote.lower())

#9
word = 'Python'
print(word[:3])
print(word[-3:])
print(word[::-1])

#10
sentence = 'I love programming in Python.'
new_sentence = sentence.replace('Python', 'Java')
print(new_sentence)

#11
text = 'The quick brown fox jumps over the lazy dog'
print('fox' in text)
print('cat' in text)


#lists
#12
fruits = ['apple', 'banana', 'cherry']
print(fruits)
fruits.append('orange')
print(fruits)
fruits.pop(0)
print(fruits)

#13
animals = ['cat', 'dog', 'rabbit', 'hamster']
print(animals[0])
print(animals[-1])
print(len(animals))

#14
numbers = [5, 10, 15, 20, 25]
numbers[1] = 12
print(numbers)
numbers.append(30)
print(numbers)
numbers.pop()
print(numbers)

#15
first_ten_numbers = list(range(1, 11))
print(first_ten_numbers[:5])
print(first_ten_numbers[-3:])
print(first_ten_numbers[::-1])

#16
list = [1, 2, 3, 4]
squares = [n**2 for n in [1, 2, 3, 4, 5]]
print(squares)

#17
fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
print(fruits.count('apple'))

#18
colors = ['red', 'blue', 'green', 'yellow', 'blue']
print(colors.index('blue'))

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(list)

#20
def remove_all(lst, value):
    return [item for item in lst if item != value]
numbers = [1, 2, 2, 3, 4, 2]
print(remove_all(numbers, 2))

#21
def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(unsorted_list))
