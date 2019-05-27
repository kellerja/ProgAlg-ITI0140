"""
Module tells Bobi where it can move.

@author: Jaanus
"""
from random import randint


def decide(sensor_data, current_state):
    """
    Decide in which direction should robot move using sensor_data.

    Use resources as efficiently as possible.
    Args:
        List of blocking objects in specific direction.
        0  - Free
        -1  - Object
        sensor_data - [n, ne, e, se, s, sw, w, nw]
    Return: One of the possible directions.
    """
    sensor_indexes = {'N': 0, 'NE': 1, 'E': 2, 'SE': 3, 'S': 4, 'SW': 5, 'W': 6, 'NW': 7}
    robot = sensor_indexes[current_state]
    movement = []
    if sensor_data[robot] == 0:
        movement.append(0)
    if sensor_data[(robot - 1) % 8] == 0:
        movement.append(-1)
    if sensor_data[(robot + 1) % 8] == 0:
        movement.append(1)
    if sensor_data[(robot + 2) % 8] == 0:
        movement.append(2)
    if sensor_data[(robot - 2) % 8] == 0:
        movement.append(-2)
    if movement == []:
        return None
    random = randint(0, len(movement) - 1)
    return movement[random]


if __name__ == "__main__":
    print("Hello from bobi.py!")
