"""Python functions for JavaScript Trials 1."""


def output_all_items(items):

    for item in items:
        print(item)

output_all_items([1, 'hello', True])



def get_all_evens(nums):
    even_numbers = []

    for num in nums:
        if num %2 ==0:
            even_numbers.append(num)
    return even_numbers
print(get_all_evens([7, 8, 10, 1, 2, 2]))



def get_odd_indices(items):
    odd_indices = []

    for idx, item in enumerate(items):
        if idx % 2 != 0:
            odd_indices.append(idx)

    return odd_indices
print(get_odd_indices([1, 'hello', True, 500]))



def print_as_numbered_list(items):
    num = 1

    for item in items:
        print(f'{num}. {item}')
        num += 1
print_as_numbered_list([1, 'hello', True])



def get_range(start, stop):
    nums = []

    for num in range(start, stop):
        nums.append(num)
    return nums
print(get_range(0,5))



def censor_vowels(word):
    chars = []

    for letter in word:
        if letter in 'aeiou':
            chars.append('*')
        else:
            chars.append(letter)

    return ''.join(chars)
print(censor_vowels('hello world'))



def snake_to_camel(string):
    camel_case = []

    for word in string.split('_'):
        camel_case.append(f'{word[0].upper()}{word[1:]}')

    return ''.join(camel_case)
print(snake_to_camel('hello_world'))



def longest_word_length(words):
    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)
    return longest

print(longest_word_length(['jellyfish', 'zebra']))




def truncate(string):
    result = []

    for char in string:
        if len(result) == 0 or char != result[len(result) -1]:
            result.append(char)

    return ''.join(result)

print(truncate('aaaabbbbcccca'))



def has_balanced_parens(string):
    parens = 0

    for char in string:
        if char == '(':
            parens += 1
        elif char == ')':
            parens -= 1

            if parens <= 0:
                return False 
    return parens <= 0

print(has_balanced_parens('()'))
print(has_balanced_parens('((This) (is) (good))'))
print(has_balanced_parens('(Oh no!)('))

def compress(string):
    compressed = []
    curr_char = ''
    char_count = 0

    for char in string: 
        if char != curr_char:
            compressed.append(curr_char)

            if char_count > 1:
                compressed.append(str(char_count))

            curr_char = char
            char_count = 0
        char_count += 1

    compressed.append(curr_char)
    if char_count > 1:
        compressed.append(str(char_count))

    return ''.join(compressed)
print(compress('aabbaabb'))










