#!/bin/bash

###############################################################################
# Your task is to use for loops to display only odd natural numbers from 1 to 
# 99.
#
# Input Format
# There is no input.
# 
# Output format
# 1 3 5 7 8 9 ... 99 
#
###############################################################################

for v in {1..99..2}
do
    echo -ne "$v "
done
