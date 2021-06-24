#!/bin/bash

# Success
# Details 
# Runtime: 0 ms, faster than 100.00% of Bash online submissions for Valid Phone Numbers.
# Memory Usage: 3.2 MB, less than 21.43% of Bash online submissions for Valid Phone Numbers.

# Read from the file file.txt and output all valid phone numbers to stdout.
grep -P '^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$' file.txt
