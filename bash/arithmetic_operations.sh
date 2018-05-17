#!/bin/bash
################################################################################
# We provide you with expressions containing +,-,*,^, / and parenthesis. None of
# the numbers in the expression involved will exceed 999.
# Your task is to evaluate the expression and display the output correct to  
# decimal places.
#
# Input Format
# -
#
# Output Format
# -
#
# Sample Input
# 5+50*3/20 + (19*2)/7
#
# Sample Output
# 17.929
################################################################################
expression="-105+50*3/20 + (19^2)/7"

LC_NUMERIC="en_US.UTF-8"
printf "%.3f\n" `echo "$expression" | bc -l`
