"""
Module that can read a text file and return it as a heatmap.

@author: Jaanus
"""
from PIL import Image
from math import log


def read_file(file):
    """Make a txt file with UTF8 encoding to a word list."""
    word_list = ''
    with open(file, 'r', encoding='UTF8') as file:
        for line in file:
            line = line.split(' ')
            new_line = ""
            for word in line:
                new_line += ' '
                for letter in word:
                    if letter.isalpha():
                        new_line += letter
                    else:
                        new_line += ' '
            word_list += new_line
    word_list = word_list.split()
    new_list = []
    for word in word_list:
        if word != '' or word != ' ':
            new_list.append(word)
    return new_list


def pair_frequency(word_list):
    """Make a list of words into a dictionary with letter pairs and the number of the pair's instances."""
    line = ' '.join(word_list)
    correct = 'ABCDEFGHIJKLMNOPQRSŠZŽTUVWÕÄÖÜXY'
    letter_pairs = {}
    for i in range(len(line) - 1):
        pair = line[i:i + 2].upper()
        if pair in letter_pairs:
            letter_pairs[pair] += 1
        elif pair[0] in correct and pair[1] in correct:
            letter_pairs[pair] = 1
    return letter_pairs


def create_heatmap(filename, pair_dictionary):
    """Make a dictionary of letter pairs into a heatmap picture with a given filename."""
    alfab = 'ABCDEFGHIJKLMNOPQRSŠZŽTUVWÕÄÖÜXY'
    size = (32, 32)
    shadeOfOne = 50
    img = Image.new('RGB', (size[0], size[1]), 'black')
    for pair in pair_dictionary.keys():
        if len(pair) == 2 and pair[0] in alfab and pair[1] in alfab:
            x = alfab.index(pair[0])
            y = alfab.index(pair[1])
            if pair_dictionary[pair] > 0:
                color = int(log(pair_dictionary[pair]) * (255 - shadeOfOne) / log(sum(pair_dictionary.values()))) + shadeOfOne
                img.putpixel((x, y), (color, color, color))
    img = img.resize((32 * 10, 32 * 10), Image.NEAREST)
    img.save(filename)

if __name__ == '__main__':
    file = read_file('carl_robert_jakobson-kolm_isamaalist_k6net.txt')
    pairs = pair_frequency(file)
    create_heatmap('carl_robert_jakobson-kolm_isamaalist_k6net.png', pairs)
