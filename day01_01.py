""" 
https://adventofcode.com/2021/day/1
https://adventofcode.com/2021/day/1/input
count the number of times a depth measurement 
increases from the previous measurement.

How many measurements are larger than the previous measurement?
"""
inc = 1

depth_file = open("C:/Users/u205863/OneDrive - Navistar/aa_python/adventofcode/2021_01_02 depths.txt","r")

depths = depth_file.readlines()

for i in range(1, len(depths)):
    if depths[i] > depths[i-1]:
        inc+=1
        
depth_file.close()
print(inc)
       
