#!/bin/bash

################################################################################
# Given three integers (X, Y, and Z) representing the three sides of a triangle,
# identify whether the triangle is Scalene, Isosceles, or Equilateral.
#
# Input Format
# Three integers, each on a new line
#
# Constraints
# 1 <= X, Y, Z <= 1000
# Sum of any two sides will be greater than the third.
#
# Output Format
# One word: either SCALENE or EQUILATERAL or ISOSCELES
#
# Sample Input
# 2
# 3
# 4
#
# Sample Output
# SCALENE
################################################################################

read x
read y
read z

if [ "$x" -lt 1 ] || [ "$y" -lt 1 ] || [ "$z" -lt 1 ]
then
    echo "Invalid input."
    exit -1;
fi

if [ "$x" -gt 1000 ] || [ "$y" -gt 1000 ] || [ "$z" -gt 1000 ]
then
    echo "Invalid input."
    exit -1;
fi

if [ ! $(($x + $y)) -gt $z ]; then
    echo "....... $(($x + $y)) > $z ?"
    echo "invalid constraint."
    exit -1;
fi

if [ $x -eq $y ] && [ $x -eq $z ]; then
    echo "EQUILATERAL"
    exit 1;
fi

if [ $x -eq $y ] || [ $x -eq $z ] || [ $y -eq $z ]; then
    echo "ISOSCELES"
    exit 1;
fi

if [ $x -ne $y ] && [ $x -ne $z ] && [ $y -ne $z ]; then
    echo "SCALENE"
    exit 1;
fi
