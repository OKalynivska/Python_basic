def append_to_list(existing_list, value_being_added):
    """ Append values to existing list

    Args:
        existing_list (list): list to which values will be added
        value_being_added (int, float, str, tuple, list, bool): value
            or values to be added to the list.

    Returns:
        list: Updated list
    """

    if (isinstance(value_being_added, list)) or (isinstance(value_being_added, tuple)):
        existing_list.extend(value_being_added)
    else:
        existing_list.append(value_being_added)
    return existing_list


list_of_numbers = [1, 2, 3]
second_list_of_numbers = [1, 23, 56]
int_single_value = 3
bool_single_value = True
str_single_value = 'test_value'
tuple_values = (1, 4, 8, 0)

print(f"int {int_single_value} added:",
      append_to_list(list_of_numbers, int_single_value))
print(f"tuple {tuple_values} added:",
      append_to_list(list_of_numbers, tuple_values))
print(f"str {str_single_value} added:",
      append_to_list(list_of_numbers, str_single_value))
print(f"list {second_list_of_numbers} added:",
      append_to_list(list_of_numbers, second_list_of_numbers))
print(f"bool {bool_single_value} added:",
      append_to_list(list_of_numbers, bool_single_value))
