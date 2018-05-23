"""
Consider a staircase of size n = 4:

   #
  ##
 ###
####

Observe that its base and height are both equal to n, and the image is drawn
using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size n.

Input Format
A single integer,n, denoting the size of the staircase.

Output Format
Print a staircase of size n using # symbols and spaces.

Note: The last line must have 0 spaces in it.

Sample Input
6

Sample Output

     #
    ##
   ###
  ####
 #####
######

Explanation
The staircase is right-aligned, composed of # symbols and spaces, and has a 
height and width of n = 6.
"""
import math
import os
import random
import re
import sys

def staircase(n):
    for i in range(0, n):
        for j in range(0, n):
            if (j >= n - i - 1):
                print("#", end ="")
            else:
                print(" ", end="")
        print("")

def main():
    number = input("give a number ")
    number = int(number)
    staircase(number)

    #print(fibonacci(number))

if __name__ == '__main__':
    main()
