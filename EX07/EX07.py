"""
EX07 - Robot decision making module

@author: Jaanus Keller
"""

import simulator


class Robot(simulator.Agent):
    """
    Class that decides robot movement.

    Is a subclass of Agent. Contains functin decide.
    """

    def __init__(self, world, x, y, direction):
        """
        Initialize the class.

        Arguments:
            world - map made by simulator module
            x and y - coordinates of the robot
            direction - direction of robot (number in between 0 and 7)
        """

        simulator.Agent.__init__(self, world, x, y, direction)

    def decide(self):
        """
        Decide where the robot moves next.

        Result:
            Gives Agent function in simulator module the next move (number between -2 and 2)
        """
<<<<<<< HEAD

        rotation = simulator.Agent.compass(self)
=======
        rotation = self.compass()
>>>>>>> 79ec15005a8d238861f72b6311a06d71ccf80e2b
        around = []
        # finds and moves to treasure
        for i in range(0, 8):
            around.append(self.detect(i))
        print(around[(rotation - 2) % 8], around[(rotation - 1) % 8], around[rotation], around[(rotation + 1) % 8], around[(rotation + 2) % 8])
        move = 0
        for i in range(-2, 0):
            if len(around[(rotation + i) % 8]) == 1:
                if around[(rotation + i) % 8][0] == -3:
                    move = i
        for i in range(0, 1):
            if len(around[(rotation + i) % 8]) == 1:
                if around[(rotation + i) % 8][0] == -3:
                    move = i
        for i in range(1, 3):
            if len(around[(rotation + i) % 8]) == 1:
                if around[(rotation + i) % 8][0] == -3:
                    move = i

        for i in range(-2, 3):
            if len(around[(rotation + i) % 8]) == 3:
                if around[(rotation + i) % 8][0] == -3:
                    move = (i - 1) % 3
        for i in range(-2, 3):
            if len(around[(rotation + i) % 8]) == 3:
                if around[(rotation + i) % 8][1] == -3:
                    move = i
        for i in range(-2, 3):
            if len(around[(rotation + i) % 8]) == 3:
                if around[(rotation + i) % 8][2] == -3:
                    move = (i + 1) % 3
        # avoids walls and obstacles
        if len(around[rotation]) == 3:
            if around[rotation][1] == -1:
                move = 1
            elif around[rotation][1] == -2:
                move = 1
            elif around[rotation][1] != 111 and around[rotation][1] != -3:  # until add other robot movement rules
                move = 1
        else:
            if around[rotation][0] == -1 and len(around[(rotation + 1) % 8]) == 1 and around[(rotation + 1) % 8][0] == -1 and len(around[(rotation - 1) % 8]) == 1 and around[(rotation - 1) % 8][0] == -1:
                move = 2
            elif around[rotation][0] == -1:
                move = 1
            elif around[rotation][0] == -2:
                move = 1
            elif around[rotation][0] != 111 and around[rotation][0] != -3:  # until add other robot movement rules
                move = 2
        if len(around[(rotation + 1) % 8]) == 1 and around[(rotation + 1) % 8][0] == -1 and len(around[(rotation + 2) % 8]) == 1 and around[(rotation + 2) % 8][0] == -1:
            move = -1
        self.turn_and_drive_straight(move) # always turn right, you have to change this obviously.

if __name__ == "__main__":
    world = simulator.World(width=10, height=10, sleep_time=0.5, reliability=1, treasure=None, obstacles=[(3, 4)])
    robots = []
    robots.append(Robot(world, 9, 1,0))
    robots.append(Robot(world, 2, 0, 1))# add more robots here if you like
    for _ in range(50): # Simulate 50 ticks
        world.print_state()
        for robot in robots:
            robot.decide()
        world.print_state()
        world.tick()
