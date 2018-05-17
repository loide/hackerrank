#!/bin/bash

# Create a program that block itself from running twice simultaneously.

if [ ! -f /tmp/lock.* ]; then
    touch /tmp/lock.$USER
    echo "process running..."
else
    echo "Process already started by another user. Aborting ..."
    exit
fi

# delay for 10 seconds
echo "Hi, im sleeping for 10 seconds"
sleep 10s

echo "finishing the process."
rm /tmp/lock.$USER
