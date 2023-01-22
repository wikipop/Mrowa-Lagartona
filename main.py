"""
    Mrowa Lagatona
    Wiktor Popiołek
"""

import random
import numpy as np

board = [[" " for x in range(10)] for y in range(10)]
ants = []


def main(n, ants_n) -> None:
    """
    :param n: Ilość kroków, które ma pokonać mrówka
    :param ants_n: Ilość mrówek
    """

    cords = {(random.randint(0, 9), random.randint(0, 9)) for x in range(ants_n)}

    if len(cords) != ants_n:
        main(n, ants_n)

    for cord in cords:
        ants.append(Ant(cord[0], cord[1]))

    for i in range(n):
        for ant in ants:
            ant.move()


class Ant:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self.direction = 0
        self.direction = random.randint(0, 3)  # 0 LEFT, 1 UP, 2 RIGHT, 3 DOWN

    def move(self):
        if board[self.x][self.y] == " ":
            board[self.x][self.y] = "#"
        else:
            board[self.x][self.y] = " "

        if self.direction == 0:
            self.x = self.x - 1 if self.x > 0 else 9
        elif self.direction == 1:
            self.y = self.y + 1 if self.y < 9 else 0
        elif self.direction == 2:
            self.x = self.x + 1 if self.x < 9 else 0
        elif self.direction == 3:
            self.y = self.y - 1 if self.y > 0 else 9

        if board[self.x][self.y] == " ":
            self.direction = self.direction + 1 if self.direction < 3 else 0
        else:
            self.direction = self.direction - 1 if self.direction > 0 else 3


def show_board():
    print(np.matrix(board))


if __name__ == '__main__':
    main(10, 10)
    show_board()
