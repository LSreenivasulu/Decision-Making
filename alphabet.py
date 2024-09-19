***
Write a program to check whether the given character is vowel or consonant.
Input format:
The input consist of a character
Output format:
The output consists of a below-given string
“Vowel” / “Consonant” / “Not an alphabet”
Sample Input:
e

Sample Output:
Vowel
***
char = input()
if len(char) == 1 and char.isalpha():
    if char.lower() in 'aeiou':
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Not an alphabet")
