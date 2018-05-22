#!/bin/bash

################################################################################
# Given N integers, compute their average correct to three decimal places.
# 
# Input Format
# The first line contains an integer, N.
# N lines follow, each containing a single integer.
# 
# Output Format
# Display the average of the N integers, rounded off to three decimal places.
# 
# Input Constraints
# 1 <= N <= 500
# -10000 <= x <= 10000 (x refers to elements of the list of integers for which
# the average is computed)
#
# Sample Input
# 4
# 1
# 2
# 9
# 8
#
# Sample Output
# 5.000
#
# Explanation
# The '4'in the first line indicates that there are four integers whose average 
# is to be computed. The average = (1 + 2+ 9 + 8)/4 = 20/4 = 5.000 (correct to
# three decimal places). Please include the zeroes even if they are redundant
# (e.g. 0.0000 instead of 0)
#
################################################################################

read size
sum=0

if [ "$size" -lt 1 ] || [ "$size" -gt 500 ]; then
    echo "Invalid Input."
    exit -1
fi

for i in $(seq 1 $size)
do
    read x
    if [ "$x" -lt -10000 ] || [ "$x" -gt 10000 ]; then
        echo "Invalid Input."
        exit -1
    fi
    sum=$(awk "BEGIN {print $sum+$x; exit}")
done
printf "%.3f\n" $(bc -l <<< "$sum/$size")
