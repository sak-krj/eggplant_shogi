from itertools import islice
# from eggplant import piecetype
from eggplant.piecetype import PieceType as PT

class Position:

    PIECE_STR = ("   "," 歩"," 香"," 桂"," 銀"," 金"," 角"," 飛"," 玉"," と"," 杏"," 圭"," 全"," 金"," 馬"," 竜","   ","v歩","v香","v桂","v銀","v金","v角","v飛","v玉","vと","v杏","v圭","v全","v金","v馬","v竜")
    BASE_POS = [(1,1,1,1,1,1,1,1,1), (0,6,0,0,0,0,0,7,0), (2,3,4,5,8,5,4,3,2)]
    TO_DAN = ("","一","二","三","四","五","六","七","八","九")

    def __init__(self):
        # self.board = [[0 for siji in range(11)] for dan in range(11)]
        self.initialize_board()

    def initialize_board(self):
        self.clear_holding()
        self.clear_board()
        # 敵陣の配置
        for d,posbydan in enumerate(reversed(Position.BASE_POS), 1):
            for s,p in enumerate(reversed(posbydan), 1):
                self.board[d][s] = p + PT.ENEMY.value
        # 自陣の配置
        for d,posbydan in enumerate(Position.BASE_POS,7):
            for s,p in enumerate(posbydan,1):
                self.board[d][s] = p
        
    def clear_board(self):
        self.board = [[PT.EMPTY.value if Position.in_board(d,s) else PT.OUT_OF_BOARD.value for s in range(11)] for d in range(11)]

    def clear_holding(self):
        self.holding = [[0 for _ in range(8)] for _ in range(2)]

    def show(self):
        print("先手 持ち駒")
        for p in self.holding[0]:
            if p == 1:
                print("{} ".format(Position.PIECE_STR[p]))
            elif p > 1:
                print("{}{} ".format(Position.PIECE_STR[p], p))
        print("")
        print("  　９　８　７　６　５　４　３　２　１ ")
        print("  +---+---+---+---+---+---+---+---+---+")

        for dan in range(1,10):
            print("{}|".format(Position.TO_DAN[dan]), end="")
            for suji in range(9, 0, -1):
                print("{}|".format(Position.PIECE_STR[self.board[dan][suji]]), end="")
            print()
        print("  +---+---+---+---+---+---+---+---+---+")
        print()
        print("後手 持ち駒 ")
        for p in self.holding[1]:
            if p == 1:
                print("{} ".format(Position.PIECE_STR[p]))
            elif p > 1:
                print("{}{} ".format(Position.PIECE_STR[p], p))
        print()
    @staticmethod
    def in_board(dan,suji):
        return (1 <= dan <= 9 and 1 <= suji <= 9)