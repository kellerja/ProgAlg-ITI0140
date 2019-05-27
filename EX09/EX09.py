"""
Module with the help from MockService uses Monte Carlo simulation on an area.

@author: Jaanus
"""
from MockService import MockService
from random import randint


class MonteCarloSimulation(object):

    """
    Class that has get_area function.

    Arguments
        object - file on which area can be calculated.
    """

    def __init__(self, service):
        """
        Constructor for the simulation.

        Arguments:
            Input service
        """
        self.service = service
        self.height = self.service.get_height()
        self.width = self.service.get_width()
        self.area = self.service.get_area()
        self.tries = self.service.tries_left()

    def get_area(self):
        """Using Monte Carlo method the function calculates area ratio."""
        dic = {}
        for _ in range(self.tries):
            x = randint(0, self.width - 1)
            y = randint(0, self.height - 1)
            target = self.service.info(x, y)
            if target in dic.keys():
                dic[target] += 1
            else:
                dic[target] = 1
        for index in dic.keys():
            dic[index] = dic[index] / self.tries * self.area
        return dic


if __name__ == "__main__":
    service1 = MockService('circle_10.txt')
    service2 = MockService('circle_100.txt')
    service3 = MockService('circle_20.txt')
    service4 = MockService('circle_200.txt')
    service5 = MockService('squares.txt')

    sim1 = MonteCarloSimulation(service1)
    sim2 = MonteCarloSimulation(service2)
    sim3 = MonteCarloSimulation(service3)
    sim4 = MonteCarloSimulation(service4)
    sim5 = MonteCarloSimulation(service5)

    print(sim1.get_area())
    print(sim2.get_area())
    print(sim3.get_area())
    print(sim4.get_area())
    print(sim5.get_area())
