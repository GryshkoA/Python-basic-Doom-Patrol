
# import keyword
# print(keyword.kwlist)
# 1. Define the id of next variables:
int_a = 55
print(id(int_a))
# 9790720
str_b = 'cursor'
print(id(str_b))
# 140220110977840

set_c = {1, 2, 3}
print(id(set_c))
# 140220110944512

lst_d = [1, 2, 3]
print(id(lst_d))
# 140220111851072

dict_e = {'a': 1, 'b': 2, 'c': 3}
print(id(dict_e))
# 140220111802944

# 2. Append 4 and 5 to the lst_d and define the id one more time.

lst_d = [1, 2, 3, 4, 5]
print(id(lst_d))
# 140220110946880
lst_d[3] = 6
print(lst_d)
print(id(lst_d))
# [1, 2, 3, 6, 5]
# 140097986646592

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