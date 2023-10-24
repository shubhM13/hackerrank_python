/*
You are given a spreadsheet that contains a list of  athletes and their details (such as age, height, weight and so on). You are required to sort the data based on the th attribute and print the final resulting table. Follow the example given below for better understanding.

image

Note that  is indexed from  to , where  is the number of attributes.

Note: If two attributes are the same for different rows, for example, if two atheletes are of the same age, print the row that appeared first in the input.

Input Format

The first line contains  and  separated by a space.
The next  lines each contain  elements.
The last line contains .

Constraints



Each element 

Output Format

Print the  lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.

Sample Input 0

5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1
Sample Output 0

7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
Explanation 0

The details are sorted based on the second attribute, since  is zero-indexed.
*/

#!/bin/python3

import math
import os
import random
import re
import sys

def print_2d_arr(arr) -> None:
    n = len(arr)
    m = len(arr[0])
    for i in range(0, n):
        for j in range(0, m):
            print(arr[i][j], end='')
            print(" ", end='')
        print()
        
def sort_2d_array(n, m, arr, k) -> None:
    # bubble sort
    for i in range(0, n):
        for j in range(0, n-i-1):
            if arr[j][k] > arr[j+1][k]:
                # tuple unpacking
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print_2d_arr(arr)
            


if __name__ == '__main__':
    first_mult_input = input().strip().split()
    n = int(first_mult_input[0])
    m = int(first_mult_input[1])
    
    arr = []
    
    for _ in range(n):
        arr.append(list(map(int, input().strip().split())))
        
    k = int(input().strip())
    
    sort_2d_array(n, m, arr, k)
    
