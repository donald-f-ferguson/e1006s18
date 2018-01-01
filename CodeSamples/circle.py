#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 10:38:37 2018

@author: donaldferguson
"""

# This program allows a user to input the radius on a circle.
# We want to teach the formula to young children. So, we only
# allow the radius to be an integer.

# Almost every program you write will use "programs" others have written.
# Your successful programs will become programs that others use.
# Any non-trivial program requires a team. The team members assemble
# the solution from individual subcomponents they build.
# The subcomponents and reusable parts are called modules.

import math     # We just imported our first module.

# Programs, like mathematical functions, are only useful if they
# operate on many user provided inputs. To start, we will get the input from
# the "command line."

# Print a prompt asking for the radius.
# Set a variable to the input value.
radius_str = input('Enter the radius of a circle: ')

# Let's double check that we got the input.
print("You entered ", radius_str, " which is of type ", type(radius_str))

# We are going to do 'math' on the input. So, we should
# covert it to an Integer.
radius_int = int(radius_str)

# The circumfrence is 2 times pi time the radius.
# The area is pi * r squared.
circumference = 2 * math.pi * radius_int
area = math.pi * (radius_int ** 2)

# Python conventions do not like lines that are too long.
# \ means that we will continue the command on the next line.
print ("The cirumference is:",circumference,  \
      ", and the area is:",area)