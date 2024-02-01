Problem: Check if an integer array contains two of the same numbers anywhere. Nested for loops will not suffice.

Solution:
Use a Hash Set to store each value checked in memory. If current number exists in hash set, return true. Else add it to set.