#!/bin/bash

# Check if correct number of arguments are passed
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <file> <new_value>"
    exit 1
fi

FILE=$1
NEW_VALUE=$2


# Use sed to replace the value of REAL_DATA_SIZE
sed -i "s/^export REAL_DATA_SIZE=.*/export REAL_DATA_SIZE=$NEW_VALUE/" "$FILE"

echo "REAL_DATA_SIZE updated to $NEW_VALUE in $FILE"
echo "REAL_DATA_SIZE updated to $NEW_VALUE in $FILE"
echo "REAL_DATA_SIZE updated to $NEW_VALUE in $FILE"
echo "REAL_DATA_SIZE updated to $NEW_VALUE in $FILE"
echo "REAL_DATA_SIZE updated to $NEW_VALUE in $FILE"
echo "REAL_DATA_SIZE updated to $NEW_VALUE in $FILE"
echo "REAL_DATA_SIZE updated to $NEW_VALUE in $FILE"
echo "REAL_DATA_SIZE updated to $NEW_VALUE in $FILE"
echo "REAL_DATA_SIZE updated to $NEW_VALUE in $FILE"
echo "REAL_DATA_SIZE updated to $NEW_VALUE in $FILE"
echo "REAL_DATA_SIZE updated to $NEW_VALUE in $FILE"
echo "REAL_DATA_SIZE updated to $NEW_VALUE in $FILE"
echo "REAL_DATA_SIZE updated to $NEW_VALUE in $FILE"
echo "REAL_DATA_SIZE updated to $NEW_VALUE in $FILE"
echo "REAL_DATA_SIZE updated to $NEW_VALUE in $FILE"
echo "REAL_DATA_SIZE updated to $NEW_VALUE in $FILE"
echo "REAL_DATA_SIZE updated to $NEW_VALUE in $FILE"
echo "REAL_DATA_SIZE updated to $NEW_VALUE in $FILE"
echo "REAL_DATA_SIZE updated to $NEW_VALUE in $FILE"
echo "REAL_DATA_SIZE updated to $NEW_VALUE in $FILE"
echo "REAL_DATA_SIZE updated to $NEW_VALUE in $FILE"
echo "REAL_DATA_SIZE updated to $NEW_VALUE in $FILE"
echo "REAL_DATA_SIZE updated to $NEW_VALUE in $FILE"
echo "REAL_DATA_SIZE updated to $NEW_VALUE in $FILE"
echo "REAL_DATA_SIZE updated to $NEW_VALUE in $FILE"
echo "REAL_DATA_SIZE updated to $NEW_VALUE in $FILE"

