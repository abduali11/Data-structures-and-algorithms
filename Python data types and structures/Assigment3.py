"Write a program that prints a dictionary where the keys are numbers between 1 and N, and the values are square of keys."

"Input Specification"

"The first line of input contains N Output Specification"

"Print the dictionary"

"The output from your program, when called with the code in the Test column, should be exactly as shown in the Result column:"

test = input("")
dictionary = {}

for i in range(int(test)):
    n = i + 1
    dictionary[n] = n*n
print(dictionary)
