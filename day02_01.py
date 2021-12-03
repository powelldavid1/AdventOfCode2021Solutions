""" 
https://adventofcode.com/2021/day/2

"""
horizontal_pos = 0
vertical_pos = 0

INPUT_FILE = '2021_d02_p1 directions.txt'

with open(INPUT_FILE,"r") as f:
    directions = f.readlines()
sub_dir = 