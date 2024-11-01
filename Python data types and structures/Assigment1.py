"Write a program that takes a single string as its input"
"sanat on wikipedia ja assume"

"and sort its characters fromthe lowest Unicode value to the highest Unicode value"

"The program should print the new string."

word1 = "wikipedia"
word2 = "assume"

print("".join(sorted(word1)))
print("".join(sorted(word2)))

"Sen voi tehdä myös tällä tavalla"
input_string = input()
print("".join(sorted(input_string)))
