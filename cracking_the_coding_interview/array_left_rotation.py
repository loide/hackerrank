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
