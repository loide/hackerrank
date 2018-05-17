#!/bin/bash

################################################################################
# Create a script that create folders reading input names on a file.
#
# Input file:
# Namibia
# Nauru
# Nepal
# Netherlands
# NewZealand
# Nicaragua
# Niger
# Nigeria
# NorthKorea
# Norway
#
################################################################################

if [ $# -ne 1 ]; then
    echo "usage: ./createfolders <input-filename>"
    exit 1;
fi

while IFS='' read -r line || [[ -n "$line" ]]; do
    echo "mkdir $line"
    mkdir $line
done < "$1"
