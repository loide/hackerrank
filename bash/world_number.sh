#!/bin/bash
################################################################################
# Given two integers,  and , find their sum, difference, product, and quotient.
#
# Input Format
# Two lines containing one integer each ( and , respectively).
#
# Constraints
# -100 <= X, Y <= 100
#
# Output Format
# Four lines containing the sum (), difference (), product (), and quotient (),
# respectively. (While computing the quotient, print only the integer part.)
#
# Sample Input
# 5
# 2
#
# Sample Output
# 7
# 3
# 10
# 2
################################################################################

# enter a number
read x

# enter another number
read y

echo ""
echo $((x + y))
echo $((x - y))
echo $((x * y))
echo $((x / y))
