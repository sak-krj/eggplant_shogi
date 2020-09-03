from eggplant.types import Types

class Move():

    def __init__(self, src, dist, piecetype, promoted, color):
        self.src = src
        self.dist = dist
        self.piecetype = piecetype
        self.promoted = promoted
        self.color = color

    def show(self):
        print("先手番" if self.color == 0 else "後手番")
        if self.src[0] != 0:
            print("{}{} → ".format(*self.src), end="")
        print("{}{}".format(*self.dist), end="")
        print("{}".format(Types.PIECE_STR[self.piecetype.value]), end="")
        if self.src[0] == 0:
            print("打  ")
        elif self.promoted:
            print("成")
        else:
            print("  ")