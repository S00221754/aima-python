def print_list_recursively(lst):
    if not lst:
        return
    
    print(lst[0])


    print_list_recursively(lst[1:])


my_list = [1, 2, 3, 4, 5]
print("List")
print_list_recursively(my_list)

def print_list_in_reverse(lst):
    if not lst:
        return
    
    print_list_in_reverse(lst[1:])
    print(lst[0])
    
print("Reverse List")
print_list_in_reverse(my_list)

def separate_list(input_list):
    atoms = []
    integers = []

    for item in input_list:
        if isinstance(item, int):
            integers.append(item)
        elif isinstance(item, str):
            atoms.append(item)

    return atoms, integers

Atoms, Integers = separate_list([1, 'a', 2, 'b', 3, 'c'])
print("Atoms:", Atoms)
print("Integers:", Integers) 


