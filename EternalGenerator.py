import random


def eternal_generator(list_of_values):
    for value in list_of_values:
        yield value
    while True:
        yield random.choice(list_of_values)


list_str = ['Java', 'Python', 'C++', 'C#', 'Pascal']

gen = eternal_generator(list_str)
print(type(gen))  # <class 'generator'>
for _ in range(10):
    print(next(gen))

# Java
# Python
# C++
# C#
# Pascal
# C#
# Java
# Pascal
# C#
# C++
