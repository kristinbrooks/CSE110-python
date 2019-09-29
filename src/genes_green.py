# Write a program to calculate the resources needed
# to remodel a golf course hole.
#     See assignment description for details.
#
# The inputs should be:
#     Enter Course Length:
#     Enter Course Width:
#
# The outputs should be:
#     Total square yards of rough sod:
#     Total square yards of smooth sod:
#     Tons of sand:
#     Number of retaining wall bricks:
#     Number of bushes:
#     Total Mowing Time (mins):

import math


def calculate_area_of_both_greens_sq_yrds(width):
    diameter_of_green_yrds = width / 2
    radius_of_green_yrds = diameter_of_green_yrds / 2
    area_of_green_sq_yrds = math.pi * radius_of_green_yrds ** 2  # area of one of the greens
    area_of_both_greens_sq_yrds = area_of_green_sq_yrds * 2  # area of both the hole green and the tee-off green
    return area_of_both_greens_sq_yrds


def calculate_smooth_sod_sq_yrds(width):
    rounded_sq_yrds_smooth_sod = math.ceil(calculate_area_of_both_greens_sq_yrds(width))
    return rounded_sq_yrds_smooth_sod


def calculate_radius_of_sand_trap_yrds(width):
    diameter_of_sand_trap_yrds = width / 3
    radius_of_sand_trap_yrds = diameter_of_sand_trap_yrds / 2
    return radius_of_sand_trap_yrds


def calculate_area_sand_trap_sq_yrds(width):
    area_of_sand_trap_sq_yrds = math.pi * calculate_radius_of_sand_trap_yrds(width) ** 2
    return area_of_sand_trap_sq_yrds


def calculate_cubic_ft_of_sand(width):
    sq_ft_per_sq_yrd = 9
    area_of_sand_trap_sq_ft = calculate_area_sand_trap_sq_yrds(width) * sq_ft_per_sq_yrd
    depth_of_sand_ft = 1
    volume_of_sand_trap_cubic_ft = area_of_sand_trap_sq_ft * depth_of_sand_ft
    return volume_of_sand_trap_cubic_ft


def calculate_tons_of_sand(width):
    lbs_per_cubic_ft = 100
    lbs_of_sand = calculate_cubic_ft_of_sand(width) * lbs_per_cubic_ft
    lbs_per_ton = 2000
    tons_of_sand = lbs_of_sand / lbs_per_ton
    rounded_tons_of_sand = math.ceil(tons_of_sand)
    return rounded_tons_of_sand


def calculate_circumference_of_sand_trap_yrds(width):
    circumference_of_sand_trap_yrds = 2 * math.pi * calculate_radius_of_sand_trap_yrds(width)
    return circumference_of_sand_trap_yrds


def calculate_number_of_bricks_for_retaining_wall(width):
    half_circumference_of_sand_trap_yrds = calculate_circumference_of_sand_trap_yrds(width) / 2
    half_circumference_of_sand_trap_ft = half_circumference_of_sand_trap_yrds * 3
    length_of_brick_ft = 1
    number_bricks_one_row = half_circumference_of_sand_trap_ft / length_of_brick_ft
    rounded_number_of_bricks_one_row = math.ceil(number_bricks_one_row)
    total_number_of_rows = 3
    rounded_bricks_three_rows = rounded_number_of_bricks_one_row * total_number_of_rows
    return rounded_bricks_three_rows


def calculate_area_of_course_sq_yrds(length, width):
    area_of_course_sq_yrds = length * width
    return area_of_course_sq_yrds


def calculate_rough_sod_sq_yrds(length, width):
    rough_sod_sq_yrds = calculate_area_of_course_sq_yrds(length, width) - calculate_area_of_both_greens_sq_yrds(width) \
                        - calculate_area_sand_trap_sq_yrds(width)
    return rough_sod_sq_yrds


def calculate_rounded_rough_sod_sq_yrds(length, width):
    rounded_rough_sod_sq_yrds = math.ceil(calculate_rough_sod_sq_yrds(length, width))
    return rounded_rough_sod_sq_yrds


def calculate_perimeter_of_course_yrds(length, width):
    perimeter_of_course_yrds = 2 * length + 2 * width
    return perimeter_of_course_yrds


def calculate_number_of_bushes(length, width):
    bushes_per_yard = 1
    missing_bushes_for_entry_and_exit = 2
    number_of_bushes = calculate_perimeter_of_course_yrds(length, width) / bushes_per_yard \
                       - missing_bushes_for_entry_and_exit
    rounded_number_of_bushes = math.floor(number_of_bushes)
    return rounded_number_of_bushes


def calculate_time_to_mow_minutes(length, width):
    time_to_mow_rough_sod_seconds_per_yrd = 0.5
    time_to_mow_smooth_sod_seconds_per_yrd = 1
    seconds_per_minute = 60
    seconds_to_mow_rough_sod = calculate_rough_sod_sq_yrds(length, width) * time_to_mow_rough_sod_seconds_per_yrd
    minutes_to_mow_rough_sod = seconds_to_mow_rough_sod / seconds_per_minute
    seconds_to_mow_smooth_sod = calculate_area_of_both_greens_sq_yrds(width) * time_to_mow_smooth_sod_seconds_per_yrd
    minutes_to_mow_smooth_sod = seconds_to_mow_smooth_sod / seconds_per_minute
    time_to_mow_course_minutes = minutes_to_mow_rough_sod + minutes_to_mow_smooth_sod
    rounded_time_to_mow_course_minutes = math.ceil(time_to_mow_course_minutes)
    return rounded_time_to_mow_course_minutes


course_length_yrds = float(input("Enter Course Length: "))
course_width_yrds = float(input("Enter Course Width: "))

total_rough_sod_sq_yrds = calculate_rounded_rough_sod_sq_yrds(course_length_yrds, course_width_yrds)
total_smooth_sod_sq_yrds = calculate_smooth_sod_sq_yrds(course_width_yrds)
total_tons_of_sand = calculate_tons_of_sand(course_width_yrds)
number_retaining_wall_bricks = calculate_number_of_bricks_for_retaining_wall(course_width_yrds)
total_number_of_bushes = calculate_number_of_bushes(course_length_yrds, course_width_yrds)
total_mowing_time_minutes = calculate_time_to_mow_minutes(course_length_yrds, course_width_yrds)

print(f"Total square yards of rough sod: {total_rough_sod_sq_yrds}")
print(f"Total square yards of smooth sod: {total_smooth_sod_sq_yrds}")
print(f"Tons of sand: {total_tons_of_sand}")
print(f"Number of retaining wall bricks: {number_retaining_wall_bricks}")
print(f"Number of bushes: {total_number_of_bushes}")
print(f"Total Mowing Time (mins): {total_mowing_time_minutes}")
