import numpy as np

matrix=[[0,0,0,0,0],
        [0,0,0,0,0],
        [0,1,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]]

swap_count=0

i=2
matrix[i], matrix[i - 1] = matrix[i - 1], matrix[i]  
swap_count += 1 

print(swap_count)