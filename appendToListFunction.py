def appendToList(existing_list, value_being_added):
    if (isinstance(value_being_added, list)) or (isinstance(value_being_added, tuple)):
        existing_list.extend(value_being_added)
    else:
        existing_list.append(value_being_added)
    return existing_list


list_of_numbers = [1, 2, 3]
second_list_of_numbers = [1, 23, 56]
single_value = 3
str_single_value = "test_value"
tuple_values = (1, 4, 8, 0)

print(appendToList(list_of_numbers, single_value))
print(appendToList(list_of_numbers, tuple_values))
print(appendToList(list_of_numbers, str_single_value))
print(appendToList(list_of_numbers, second_list_of_numbers))
