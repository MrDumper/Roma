list_of_numbers = [19, 13, 29, 18, 26, 38]
result = filter(lambda x: x % 19 == 0 or x % 13 == 0, list_of_numbers)
print(list(result))