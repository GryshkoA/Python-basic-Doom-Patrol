# import keyword
# print(keyword.kwlist)
# 1. Define the id of next variables:
int_a = 55
print(id(int_a))
# 9790720
str_b = 'cursor'
print(id(str_b))
# 140111303752560

set_c = {1, 2, 3}
print(id(set_c))
# 140111303719168

lst_d = [1, 2, 3]
print(id(lst_d))
# 140111304625792

dict_e = {'a': 1, 'b': 2, 'c': 3}
print(id(dict_e))
# 140111304577600

# 2. Append 4 and 5 to the lst_d and define the id one more time.


lst_d.append(4)
print(lst_d)
# [1, 2, 3, 4]
lst_d.append(5)
print(lst_d)
# [1, 2, 3, 4, 5]
print(id(lst_d))
# 140111304625792

# 3. Define the type of each object from step 1.
print(type(int_a))
# <class 'int'>
print(type(str_b))
# <class 'str'>
print(type(set_c))
# <class 'set'>
print(type(lst_d))
# <class 'list'>
print(type(dict_e))
# <class 'dict'>

# 4. Check the type of the objects by using isinstance.

# String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."
int_a = 55
print(isinstance(int_a, int))
# True

str_b = 'cursor'
print(isinstance(str_b, str))
# True
set_c = {1, 2, 3}
print(isinstance(set_c, set))
# True
lst_d = [1, 2, 3]
print(isinstance(lst_d, list))
# True
dict_e = {'a': 1, 'b': 2, 'c': 3}
print(isinstance(dict_e, dict))
# True


print("Anna has 5 apples and 1 peaches.")
# Anna has 5 apples and 1 peaches.

# 5. With .format and curly braces {}
print("Anna has {} apples and {} peaches.".format(5, 1))
# Anna has 5 apples and 1 peaches.

# 6. By passing index numbers into the curly braces
print("Anna has {1} apples and {0} peaches.".format("6", "2"))
# Anna has 2 apples and 6 peaches.

# 7. By using keyword arguments into the curly braces.
print("Anna has {q} apples and {w} peaches.".format(q="red", w="sweet"))
# Anna has red apples and sweet peaches.

# 8*. With indicators of field size (5 chars for the first and 3 for the second)

print("Anna has {0:5} apples and {1:3} peaches.".format("red", "sweet"))
# Anna has red   apples and sweet peaches.

# 9. With f-strings and variables

a = 5
b = 1
print(f"Anna has {a} apples and {b} peaches.")
# Anna has 5 apples and 1 peaches.

# 10. With % operator
a = 5
b = 1
print("Anna has %s apples and %s peaches." % (a, b))
# Anna has 5 apples and 1 peaches.

# 11*. With variable substitutions by name (hint: by using dict)
name = "red"
color = "green"
data_dict = {"ap": name, "pch": color}
print('Anna has %(ap)s apples and %(pch)s peaches.' % data_dict)
# Anna has red apples and green peaches.

# Comprehensions:
# (1)
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)
print(lst)
# 2. Convert (1) to list comprehension
list_comprehension = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(list_comprehension)
# [0, 1, 16, 9, 256, 25, 1296, 49, 4096, 81]

# 13. Convert (2) to regular for with if-else
list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
lst = []
for num in range(10):
    if num % 2 == 0:
        lst.append(num // 2)
    else:
        lst.append(num * 10)
        print(lst)
# [0, 10]
# [0, 10, 1, 30]
# [0, 10, 1, 30, 2, 50]
# [0, 10, 1, 30, 2, 50, 3, 70]
# [0, 10, 1, 30, 2, 50, 3, 70, 4, 90]

# 14. Convert (3) to dict comprehension.
dict_comprehension = {a: a ** 2 for a in range(1, 11) if a ** 2 % 2 == 1}
print(dict_comprehension)
# {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
# (3)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
print(d)
# 15*. Convert (4) to dict comprehension.

dict_comprehension = {a: a ** 2 if a ** 2 % 2 == 1 else a // 0.5 for a in range(1, 11)}
print(dict_comprehension)
# {1: 1, 2: 4.0, 3: 9, 4: 8.0, 5: 25, 6: 12.0, 7: 49, 8: 16.0, 9: 81, 10: 20.0}
# (4)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
    else:
        d[num] = num // 0.5
print(d)
# 16. Convert (5) to regular for with if.
# (5)
d = {}
for num in range(10):
    if num ** 3 % 4 == 0:
        d[num] = num ** 3
print(d)
# {0: 0, 2: 8, 4: 64, 6: 216, 8: 512}
dict_comprehension = {x: x ** 3 for x in range(10) if x ** 3 % 4 == 0}
print(dict_comprehension)
# 17*. Convert (6) to regular for with if-else.
d = {}
for num in range(10):
    if num ** 3 % 4 == 0:
        d[num] = num ** 3
    else:
        d[num] = num
print(d)
# (6)
dict_comprehension = {x: x ** 3 if x ** 3 % 4 == 0 else x for x in range(10)}
print(dict_comprehension)


# {0: 0, 1: 1, 2: 8, 3: 3, 4: 64, 5: 5, 6: 216, 7: 7, 8: 512, 9: 9}
# Lambda:

# 18. Convert (7) to lambda function
# (7)
# def foo(x, y):
#     if x < y:
#         return x
#     else:
#         return y
# print(foo(1, 2))

foo = lambda x, y: x if x < y else y
print(foo(1, 2))
# 1

# 19*. Convert (8) to regular function
# (8) foo = lambda x, y, z: z if y < x and x > z else y

def foo(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y


print(foo(4, 6, 1))
# 6

# 20. Sort lst_to_sort from min to max
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort))
# [1, 5, 13, 15, 18, 24, 33, 55]

# 21. Sort lst_to_sort from max to min
print(sorted(lst_to_sort, reverse=True))
# [55, 33, 24, 18, 15, 13, 5, 1]

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
list_lambda = list(map(lambda x: x * 2, lst_to_sort))
print(list_lambda)
# [10, 36, 2, 48, 66, 30, 26, 110]

# 23*. Raise each list number to the corresponding number on another list:

list_A = [2, 3, 4]
list_B = [5, 6, 7]
list_mtp = list(map(lambda x, y: x ** y, list_A, list_B))
print(list_mtp)

# 24. Use reduce and lambda to compute the numbers of a lst_to_sort.
import functools

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]

reduce_lst = functools.reduce(lambda x, y: x + y, lst_to_sort)
print(reduce_lst)
# 164

# 25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.

new_list = list(filter(lambda x: (x % 2 == 1), lst_to_sort))
print(new_list)

# [5, 1, 33, 15, 13, 55]

# 26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.

lst_negative = list(filter(lambda x: x < 0, range(-10, 10)))
print(lst_negative)
# [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

# 27*. Using the filter function, find the values that are common to the two lists:
list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]

lst_filter = list(filter(lambda x: x in list_1, list_2))
print(lst_filter)
# [2, 3, 5, 7]
