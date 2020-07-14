# 4 Finally, the Count helped us figure out how many of each letter we have in a string, and for each print them out in descending order.
# write a function that takes a string 
# and return each letter, along with how many times it occurs in the string and
def letter_count(s):
    # create a dictionary
    counts = {}

    # iterate through the string and
    for character in s:    
    # if the character is in the dictionary, increment its counter
        if character in counts:
            counts[character] += 1

    # if not, add it, with value 13
        else:
            counts[character] = 1
    # return teh dictionary
    return counts

    # Stage 2: 
    ## Print them all, but start with the key that occurs most ofthen in our strings
    ## Also: accept only letters, and ensure they are lowercase

def print_sorted_letter_count(s):

    letters = letter_count(s)

    letters_list = list(letters.items())

    letters_list.sort(key=lambda pair:[1], reverse=True)

    for pair in letters_list:
        print(f'Letter: {pair[0]}, count: {pair[1]}')

# print(letter_count('Hello'))
# print(letter_count('The quick brown fox jumps over the lazy dog'))


print_sorted_letter_count(letter_count('Hello'))

print_sorted_letter_count('The quick brown fox jumps over the lazy dog')