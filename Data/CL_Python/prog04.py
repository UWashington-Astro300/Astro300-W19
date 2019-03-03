#!/usr/bin/env python

import sys

my_program = sys.argv[0]
my_args = sys.argv[1:]
my_len = len(my_args)

my_output = ("I ran the program {0} with {1} arguments {2}"
            .format(my_program, my_len, my_args))

print(my_output)
print('\n')

my_a = float(sys.argv[1])
my_b = float(sys.argv[2])
my_answer = my_a + my_b

my_sum = ("The sum of {0} and {1} is {2}"
            .format(my_a, my_b, my_answer))

print(my_sum)
