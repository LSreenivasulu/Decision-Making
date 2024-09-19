***
There are 3 labs in the CSE department are L1, L2, and L3 with a seating capacity of x, y, and z respectively. One of the 3 labs has been allocated for ACE training. Out of the available labs, find the lab which has minimal seating capacity.
Input format:
Input consists of 3 integers and a string
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
The fourth input denotes the lab which is allocated for ACE training
Output format:
Print the minimal seating capacity lab amongst the available labs.
Refer the Sample output for formatting
Sample Input:
30
40
20
L3
Sample Output:
L1

*** 
a = int(input().strip())   
b = int(input().strip())   
c = int(input().strip())   
allocated_lab = input().strip()
minimal_lab = None
minimal_capacity = float('inf')
if allocated_lab != 'L1':
    if a < minimal_capacity:
        minimal_capacity = a
        minimal_lab = 'L1'
if allocated_lab != 'L2':
    if b < minimal_capacity:
        minimal_capacity = b
        minimal_lab = 'L2'
if allocated_lab != 'L3':
    if c < minimal_capacity:
        minimal_capacity = c
        minimal_lab = 'L3'
print(minimal_lab)
