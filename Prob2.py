'''
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index
i of the new array is the product of all the numbers in the original array
except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be
[2, 3, 6].

Follow-up: what if you can't use division?


'''
def get_multiplied_array(array):
    new_array = list()
    for item in array:
        temp_array = array[:]
        if len(temp_array) == 0:
            break
        temp_array.remove(item)
        mul = 1
        for i in temp_array:
            mul = mul * i
        new_array.append(mul)
    return new_array

print get_multiplied_array([1, 2, 3, 4, 5])
