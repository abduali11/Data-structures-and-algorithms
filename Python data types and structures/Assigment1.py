"Write a program that takes a single string as its input"
"sanat on wikipedia ja assume"

"and sort its characters fromthe lowest Unicode value to the highest Unicode value"

"The program should print the new string."

input_string = input()
print("".join(sorted(input_string)))
