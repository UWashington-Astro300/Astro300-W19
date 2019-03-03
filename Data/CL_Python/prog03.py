#!/usr/bin/env python

import sys

my_program = sys.argv[0]
my_args = sys.argv[1:]
my_len = len(my_args)

my_output = ("I ran the program {0} with {1} arguments {2}"
            .format(my_program, my_len, my_args))

print (my_output)
