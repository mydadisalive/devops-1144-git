# exercise 20
def remove_all(lst, value):
    while value in lst:
        lst.remove(value)
    return lst

numbers = [1, 2, 2, 3, 4, 2]
print(numbers)
remove_all(numbers, 2)
print(numbers)