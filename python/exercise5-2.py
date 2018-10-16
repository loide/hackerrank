"""
Think Python by Allen B. Downey
http://thinkpython.com

Exercise 5.2 Write a function called do_n that takes a function object and a 
number, n, as arguments, and that calls the given function n times.

"""
def f_function(n):
    print (str(n) + " time execution")

def do_n(n):
    if (n > 1):
        do_n(n - 1)
    f_function(n)


def main():
    n = input("give a number: ")
    n = int(n)
    do_n(n)

if __name__ == '__main__':
    main()
