# Write a program to determine how many gallons of water it would take to fill your pool,
# or your garage (if it were perfectly rectangular; ignore curves and cutouts), then calculate your water bill.

# In this challenge, you must choose your own input variables, variable names, and design your own tests to
# verify the program operation.

# The water used should be placed in an output variable called "gallons_used" and the cost should be placed in
# a variable called "water_cost"

# When you click the Run Button, your program will be executed, and the value of the "gallons_used"
# and "water_cost" variables will be printed below.

pool_width_feet = 12
pool_length_feet = 20
pool_depth_feet = 5
gallons_per_cubic_foot = 7.48052
cost_per_gallon = 0.0082

pool_volume_cubic_feet = pool_width_feet * pool_length_feet * pool_depth_feet

gallons_used = pool_volume_cubic_feet * gallons_per_cubic_foot

water_cost = gallons_used * cost_per_gallon
