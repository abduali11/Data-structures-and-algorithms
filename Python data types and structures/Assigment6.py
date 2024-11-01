"Write a function called custom_encoder that accepts a string text as parameter"

"and for each char of the text it calculates its 0-based position in the following reference string:"

"reference_string = 'abcdefghijklmnopqrstuvwxyz"

"The function should return a list that contains all the positions. "
"If a char is not found in the reference_string, its position should be -1"


def custom_encoder(text):
    reference_string = 'abcdefghijklmnopqrstuvwxyz'
    empty_list = []
    text = text.lower()

    for char in text.lower():
        if char in reference_string:
            empty_list.append(reference_string.index(char))
        else:
            empty_list.append(-1)
    return empty_list


print(custom_encoder('Hello'))



