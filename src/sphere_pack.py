# Write a program to determine how many oranges can fit into one standard shipping container.
# What if it were ping-pong balls instead?  What if it was your kitchen?

# In this challenge, you must choose your own input variables, variable names, and design your own tests to
# verify the program operation.

# The output value should be written into a variable called "packed_items"

# When you click the Run Button, your program will be executed, and the value of the "packed_items" variable will
# be printed below.

import math
math.pi

radius_of_average_orange_inches = 1.25
sphere_volume_inches_cubed = (4/3) * math.pi * radius_of_average_orange_inches ** 3

shipping_container_width_inches = 18
shipping_container_length_inches = 24
shipping_container_height_inches = 16
shipping_container_volume_inches_cubed = shipping_container_width_inches * shipping_container_length_inches *\
                                         shipping_container_height_inches

packed_items = int(shipping_container_volume_inches_cubed / sphere_volume_inches_cubed)
