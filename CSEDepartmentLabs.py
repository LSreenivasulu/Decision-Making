***
There are 3 labs in the CSE department. The labs are L1, L2, and L3 with a seating capacity of x, y, and z respectively. A single lab needs to be allocated to a class of 'n' students. The labs need to be utilized to the maximum i.e the number of systems used should not be minimal. Which lab needs to be allocated to this class?
Input format:
Input consists of 4 integers
The first input denotes 'x'
The second input denotes 'y'
The third input denotes 'z'
The fourth input denotes 'n'
Output format:
Print the lab which is suitable for  'n' number of students
Refer the Sample output for formatting
Sample Input:
30
40
20
25
Sample Output:
L1
***
x = int(input().strip())   
y = int(input().strip())   
z = int(input().strip())   
n = int(input().strip())   
best_lab = None
max_capacity = -1
if x >= n and x > max_capacity:
    max_capacity = x
    best_lab = 'L1'
if y >= n and y > max_capacity:
    max_capacity = y
    best_lab = 'L2'
if z >= n and z > max_capacity:
    max_capacity = z
    best_lab = 'L3'
if best_lab:
    print(best_lab)
else:
    print("No suitable lab available")
