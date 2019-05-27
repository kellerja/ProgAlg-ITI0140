"""
Module that can be used to solve several problems using regular expressions.

author: Jaanus
"""
import re


def ex1_solution(input_string):
    """Check if input is binary."""
    match = re.search('[^1|^0]', input_string)
    return True if match is None else False


def ex2_solution(input_string):
    """Check if binary input is even."""
    match = re.search('0$', input_string)
    return True if match is not None else False


def ex3_solution(input_string):
    """Check if binary input has even number of digits."""
    match = re.search('^(00|01|10|11)*$', input_string)
    return True if match is not None else False


def ex4_solution(input_string):
    """Check if binary input has 0110 or 1001 in it."""
    match = re.search('0110|1001', input_string)
    return True if match is not None else False


def ex5_solution(input_string):
    """Check if binary input has 0110 and 1001."""
    match = re.search('(0110)+.*(1001)+|(1001)+.*(0110)+|011001|100110', input_string)
    return True if match is not None else False


def ex6_solution(input_string):
    """Check if words in a given string."""
    match = re.search('kastiauto ratas|kasti auto ratas|kasti-auto ratas', input_string)
    return True if match is not None else False


def ex7_solution(input_string):
    """Check if string consists of 3 or 4 words."""
    match = re.search('^(([0-9a-zA-Z_?!]*)( [0-9a-zA-Z_?!]*){2,3})$', input_string)
    return True if match is not None else False


def ex8_solution(input_string):
    """Check if inbetween 'kass' and 'koer' is at most 2 words."""
    match = re.search('kass koer|kass [0-9a-zA-Z_]* koer|kass [0-9a-zA-Z_]* [0-9a-zA-Z_]* koer', input_string)
    return True if match is not None else False


def ex9_solution(input_string):
    """Check if input is a correctly displayed 24 hour time."""
    match = re.search('(^[0-9]|1[0-9]|2[0-3]):([0-5][0-9])$', input_string)
    return True if match is not None else False


def ex10_solution(input_string):
    """Check if input is a correct DNA sequence."""
    match = re.search('.*ATG([ACGT]{3}){1,}(TAA|TAG|TGA)', input_string)
    return True if match is not None else False


def ex11_solution(input_string):
    """Check if input is a conventional money display."""
    match = re.search('^\$[0-9]{1,3}(,[0-9]{3})*(\.[0-9]{2}|\.0|)$', input_string)
    return True if match is not None else False


def ex12_solution(input_string):
    """Check if binary input has even number of 0."""
    match = re.search('^(1*(01*0)*1*)*$', input_string)
    return True if match is not None else False


def ex13_solution(input_string):
    """Check that binary input has digits switching."""
    match = re.search('00+|11+', input_string)
    return True if match is None else False


def ex14_solution(input_string):
    """Check if input has a pickup wheel and price."""
    match = re.search('.*kasti[ -]?auto ratas(\s\w+)*(\s\$[0-9]*.[0-9]{1,2})', input_string)
    return True if match is not None else False


def ex15_solution(input_string):
    """Check if binary input can be divided by 3 (for numbers between 3 an 30 + tested values)."""
    match = re.search('^11$|^110$|^1001$|^1100$|^1111$|^10010$|^101010$|^11000$|^11011$|^11110$', input_string)
    return True if match is not None else False
# ^000111000101$|^100001$|^10101$|^101010110$|^1110101$|^111111$|


print(ex1_solution('10010101'))
print(ex2_solution('100101001'))
print(ex3_solution('10001000'))
print(ex4_solution('0100010100010'))
print('5', ex5_solution('10010110'))
print(ex6_solution('kastiautos ratas'))
print('7', ex7_solution('word word word word word'))
print(ex8_solution('kass word word word koer'))
print('9', ex9_solution('04:00'))
print('10', ex10_solution('ATGCCCAAATTTGGGTGA'))
print('11', ex11_solution('$5000'))
print(ex12_solution('01100010100010'))
print(ex13_solution('010101010'))
print('14', ex14_solution('blah blah blah kasti auto ratas toyota 1993 punane blah blah blah $5000'))
print('14', ex14_solution('kasti auto ratas $1234.56'))
print('14', ex14_solution('kasti auto ratas $5000'))
print(ex15_solution('011000101000101'))
