# LAB 4 ECERCISE 8

# def triple_and_filter(*nums):
#     filtered_numbers = list(filter(lambda x: x %4 == 0, nums))
#     final_numbers = map(lambda x: x+x+x, filtered_numbers)
#     return list(final_numbers)


# print(triple_and_filter(1,2,3,4))


# EXERCISE 9

def extract_full_name(*args):
    return args[0]['first'] + " " + args[0]['last']

names = [{'first': 'John', 'last': 'Doe'}, {'first': 'Jane', 'last': 'Christopher'}]

new_names = map(extract_full_name, names)

print(list(new_names))