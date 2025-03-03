def all_elements_true(t):
    return all(t)


the_list = [1, 0, 3, 4]

if all_elements_true(the_list):
    print("All elements true")
else:
    print("All elements not true")