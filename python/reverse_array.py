"""
Get a array and do a reverse.

Example:
- input: [1, 2, 3, 4]
- output: [4, 3, 2, 1]
"""

reversed_arr = []

def do_reverse(arr, arr_size):
    if (arr_size > 0):
        arr_size -= 1
        reversed_arr.append(arr[arr_size])
        do_reverse(arr, arr_size)

def main():
    arr = [1, 2, 3, 4, 5]
    print(arr)

    arr_size = len(arr)
    do_reverse(arr, arr_size)
    print(reversed_arr)

if __name__ == "__main__":
    main()
