"""
Takes in a wagon list with syntax letters in a list and reversed the members of list according to the depot length.

@author: Jaanus Keller
"""


def reorient_cars(list_of_wagons, depot_length):
    """Reverse wagons in the list according to the depot length.

    Keyword arguments:
    list_of_wagons -- wagons (default [])
    depot_length -- number of wagons proccessed at a time (default 0)

    Returns:
    reversed list_of_wagons
    """
    if depot_length <= 0:
        return list_of_wagons
    if len(list_of_wagons) > depot_length:
        n = 0
        result = []
        for i in range(len(list_of_wagons) // depot_length + 1):
            depot = []
            for element in list_of_wagons[n:depot_length + n]:
                depot.append(element)
            for train in depot[::-1]:
                result.append(train[::-1])
            n += depot_length
        return result
    else:
        result = []
        for train in list_of_wagons:
            result.append(train[::-1])
        return result[::-1]
