"""
The Fibonacci Sequence

The Fibonacci sequence begins with fibonacci(0) = 0 and fibonacci(1) = 1 as its
respective first and second terms. After these first two elements, each 
subsequent element is equal to the sum of the previous two elements.

Here is the basic information you need to calculate fibonacci(n):
    * fibonacci(0) = 0
    * fibonacci(1) = 1
    * fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)

Task
Given n, complete the fibonacci function so it returns fibonacci(n).

Input Format
Locked stub code in the editor reads a single integer denoting the value of n 
and passes it to the fibonacci function.

Constraints
0 < n <= 30

Output Format
Locked stub code in the editor prints the value of fibonacci(n) returned by 
the fibonacci function.

Sample Input
    3

Sample Output
    2
"""

def fibonacci(n):
    if (n == 0):
        return 0

    if (n == 1):
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    number = input("give a number ")
    number = int(number)

    print(fibonacci(number))

if __name__ == "__main__":
    main()
