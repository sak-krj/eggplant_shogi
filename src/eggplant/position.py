# from eggplant.types import Types
from eggplant.types import Types
from eggplant.piecetype import PieceType as PT
from eggplant.move import Move

class Position:

    BASE_POS = [(1,1,1,1,1,1,1,1,1), (0,6,0,0,0,0,0,7,0), (2,3,4,5,8,5,4,3,2)]

    def __init__(self):
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
        self.holding = [[0 for _ in range(9)] for _ in range(2)]

    def show(self):
        print("先手 持ち駒")
        for p,num in enumerate(self.holding[0]):
            if num == 1:
                print("{} ".format(Types.PIECE_STR[p]), end="")
            elif num > 1:
                print("{}{} ".format(Types.PIECE_STR[p], num), end="")
        print("")
        print("  　９　８　７　６　５　４　３　２　１ ")
        print("  +---+---+---+---+---+---+---+---+---+")

        for dan in range(1,10):
            print("{}|".format(Types.DAN_STR[dan]), end="")
            for suji in range(9, 0, -1):
                print("{}|".format(Types.PIECE_STR[self.board[dan][suji]]), end="")
            print()
        print("  +---+---+---+---+---+---+---+---+---+")
        print()
        print("後手 持ち駒 ")
        for p,num in enumerate(self.holding[1]):
            if num == 1:
                print("{} ".format(Types.PIECE_STR[p]), end="")
            elif num > 1:
                print("{}{} ".format(Types.PIECE_STR[p], num), end="")
        print()

    def move(self, move):
        piece = move.piecetype.value
        from_suji, from_dan = move.src
        to_suji, to_dan = move.dist

        taken = self.board[to_dan][to_suji]
    
        if PT.is_promoted(taken):
            taken -= PT.PROMOTED.value
        if taken != PT.EMPTY.value:
            if PT.EFU.value <= taken <= PT.ERY.value:
                taken -= PT.ENEMY.value
            self.holding[move.color][taken] += 1

        if from_suji:
            self.board[from_dan][from_suji] = PT.EMPTY.value
        else:
            self.holding[move.color][piece] -= 1

        if move.promoted:
            self.board[to_dan][to_suji] = piece + PT.PROMOTED.value 
        else:
            self.board[to_dan][to_suji] = piece

    @staticmethod
    def in_board(dan,suji):
        return (1 <= dan <= 9 and 1 <= suji <= 9)

