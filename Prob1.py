'''
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the
list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

def check_num_add(l, k):
    for i in l: 
        for j in reversed(l):
            if (j + i) == k:
                print j, i
                return True
    return False

print check_num_add([80, 98, 83, 92, 1, 38, 37, 54, 58, 89], 181)

