# Packing
x = 10, 20, 30
print(type(x))
print(x)

# Unpackings
# Tuple
nums = (1, 2, 3)
a, b, c = nums
print(a, b, c)

# List
a, b, c = [1, 2, 3]
print(a, b, c)

# Extended Unpacking
a, *b, c, d = [1, 2, 3, 4, 5, 6]
print(b, type(b))

# Packing in function parameters: *args
def sum(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum

print(sum(1, 2))

# Unpacking (Spread Operator)
def sum(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum

nums = [1, 2, 3, 4, 5]
print(sum(*nums))

# **kwargs (Dictionary packing)
def person(**props):
    print(type(props))
    print(props['name'])

person(name="Ahmad", age=10)

# Dictionary unpacking
def person(name, age):
    print(name, age)

p = {'name': 'Ahmad', 'age': 21}
person(**p)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [*list1, *list2]
print(list3, len(list3), type(list3))

p = {'name': 'Ahmad', 'age': 21}
p2 = {**p}
print(p2, len(p2), type(p2))