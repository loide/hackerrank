"""
Think Python by Allen B. Downey
http://thinkpython.com

Exercise 5.3 Fermat's Last Theorem says that there are no positive integers a,
b, and c such that 
               aˆn + bˆn = cˆn
for any values of n greater than 2.

1. Write a function named check_fermat that takes four parameters - a, b, c,
and n - and that checks to see if Fermat's theorem holds. If n is greater than
2 and it turns out to be true that 
               aˆn + bˆn = c^n
the program should print, "Holy smokes, Fermat was wrong!". Otherwise the
program should print, "No, that doesn't work.".

2. Write a function that prompts the user to input values for a, b, c and n,
converts them to integers, and uses check_fermat to check whether they violet
Fermat's theorem.
"""
import math

def check_fermat(a, b, c, n):
    fst_exponent = math.pow(a, n)
    snd_exponent = math.pow(b, n)
    thd_exponent = math.pow(c, n)

    if (fst_exponent + snd_exponent == thd_exponent):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")

def main():
    print("Test Fermat's Last Theorem")
    a = input("give a value to A: ")
    a = int(a)

    b = input("give a value to B: ")
    b = int(b)

    c = input("give a value to C: ")
    c = int(c)

    n = input("give a value to N: ")
    n = int(n)

    check_fermat(a, b, c, n)

if __name__ == "__main__":
    main()
