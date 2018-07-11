"""
Arrays: Left Rotation
Check out the resources on the page's right side to learn more about arrays. 
The video tutorial is by Gayle Laakmann McDowell, author of the best-selling 
interview book Cracking the Coding Interview.

A left rotation operation on an array shifts each of the array's elements 1 
unit to the left. For example, if 2 left rotations are performed on array 
[1,2,3,4,5], then the array would become [3,4,5,1,2].

Given an array a of n integers and a number, d, perform d left rotations on the
array. Return the updated array to be printed as a single line of 
space-separated integers.
"""
def rotLeft(a, d):
    arr_size = len(a)
    startpoint = d % arr_size
    new_arr = []

    for i in range(arr_size):
        new_arr.append(a[(startpoint + i) % arr_size])

    return new_arr

if __name__ == '__main__':
    n = 10
    d = 5
    a = [1,2,3,4,5,6,7,8,9,10]

    result = rotLeft(a, d)
    print (result)
