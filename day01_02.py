""" 
Problem #2
https://adventofcode.com/2021/day/1
https://adventofcode.com/2021/day/1/input

Considering every single measurement isn't as useful as you expected: there's just too much noise in the data.

Instead, consider sums of a three-measurement sliding window. Again considering the above example:

199  A      
200  A B    
208  A B C  
210    B C D
200  E   C D
207  E F   D
240  E F G  
269    F G H
260      G H
263        H
Start by comparing the first and second three-measurement windows. The measurements in the first window are marked 
A (199, 200, 208); their sum is 199 + 200 + 208 = 607. The second window is marked B (200, 208, 210); its sum is 618. 
The sum of measurements in the second window is larger than the sum of the first, so this first comparison increased.

Your goal now is to count the number of times the sum of measurements in this sliding window increases 
from the previous sum. So, compare A with B, then compare B with C, then C with D, and so on. Stop when there 
aren't enough measurements left to create a new three-measurement sum.

"""
inc = 1

depth_file = open("C:/Users/u205863/OneDrive - Navistar/aa_python/adventofcode/2021_01_02 depths.txt","r")

depths = depth_file.readlines()

for i in range(0, len(depths)):
    if depths[i] > depths[i-1]:
        inc+=1
        
depth_file.close()
print(inc)