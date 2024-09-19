***
Ask a user for their birth year encoded as two digits (like "62") and for the current year, also encoded as two digits (like "99"). Write a program to find the users current age in years.
Input format:
Input consists of 2 integers
The first integer corresponds to the last 2 digits of the birth year
The second integer corresponds to the last 2 digits of the current year
Output format:
Print the user's current age
Refer below sample output for formatting.
Sample Input:
62
00
Sample Output:
38

***
birth_year_last_two_digits = int(input().strip())
current_year_last_two_digits = int(input().strip())
if current_year_last_two_digits >= 0 and current_year_last_two_digits <= 99:
     current_year = 2000 + current_year_last_two_digits
else:
    raise ValueError("Invalid current year input")
if birth_year_last_two_digits >= 0 and birth_year_last_two_digits <= 99:
    if current_year_last_two_digits >= birth_year_last_two_digits:
        birth_year = 2000 + birth_year_last_two_digits
    else:
        birth_year = 1900 + birth_year_last_two_digits
else:
    raise ValueError("Invalid birth year input")
age = current_year - birth_year
print(age)
