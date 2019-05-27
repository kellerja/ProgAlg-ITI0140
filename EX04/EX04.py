"""
Makes a list that contains mines and area near the mine with appropriate value.

@author: Jaanus Keller
"""


def create_mine_map(mines, layers):
    """
    Function takes mine locations and layers as an input and outputs the safety values of an area.

    Arguments:
    mines -- places of mines (default [])
    layers -- how big is the area to map for mines (default 0)

    Returns:
    The area map with mines and values that show how many mines are near that block.
    """
    polar_map = []
# check for limits
    if layers <= 0:
        return polar_map
# create empty map that is 3 layers bigger than nessesary
    big_map = []
    for area in range(layers + 3):
        big_map.append([])
        for looping in range(4):
            big_map[area].append(0)
# remove mines that do not change map
    mines = list(set(mines))
    n = -1
    for i in range(len(mines)):
        n += 1
        if mines[n][0] >= len(big_map) or mines[n][1] >= 4:
            mines.pop(n)
            n -= 1
# mark  mines and values around mines
    for i in range(len(mines)):
        n = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
        m = [0, 1, -1, 1, -1, 0, -1, 0, 1]
        big_map[mines[i][0]][mines[i][1]] = 'X'
        if mines[i][0] == 0 and big_map[mines[i][0]][(mines[i][1] + 2) % 4] != 'X':
            big_map[mines[i][0]][(mines[i][1] + 2) % 4] += 1
            n = [0, 1, 0, 1, 0, 1]
            m = [1, -1, -1, 0, 0, 1]
        for number in range(len(n)):
            if big_map[(mines[i][0] + n[number]) % len(big_map)][(mines[i][1] + m[number]) % 4] != 'X':
                big_map[(mines[i][0] + n[number]) % len(big_map)][(mines[i][1] + m[number]) % 4] += 1
# remove the extra 3 layers
    big_map.pop(-1)
    big_map.pop(-1)
    big_map.pop(-1)
    return big_map
print(create_mine_map([(0, 0), (2, 2), (3, 3), (2, 2)], 4))
