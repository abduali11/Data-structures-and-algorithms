"Assume s is a string of lower case characters."

"Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'."

"For example, if s = 'hello', your program should print:"

"Number of vowels: 2"

s = input("kirjoita sana ")

vowels = "aeiou"
maara = 0

for char in s:
    if char in vowels:
        maara +=1
print(f"vookaleja on {maara} kappaletta")