from eggplant.piecetype import PieceType as PT

class Position:

    PIECE_STR = ("   "," 歩"," 香"," 桂"," 銀"," 金"," 角"," 飛"," 玉"," と"," 杏"," 圭"," 全"," 金"," 馬"," 竜","   ","v歩","v香","v桂","v銀","v金","v角","v飛","v玉","vと","v杏","v圭","v全","v金","v馬","v竜")
    BASE_POS = [(1,1,1,1,1,1,1,1,1), (0,6,0,0,0,0,0,7,0), (2,3,4,5,8,5,4,3,2)]
    TO_DAN = ("","一","二","三","四","五","六","七","八","九")

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

    def move(self, move_info):
        piece = move_info.piecetype.value
        from_suji, from_dan = move_info.src
        to_suji, to_dan = move_info.dist

        turn = True if PT.FU.value <= piece <= PT.RY.value else False

        taken = self.board[to_dan][to_suji]
        if PT.is_promoted(taken):
            taken -= PT.PROMOTED.value
        if taken != PT.EMPTY.value:
            self.holding[turn][taken]

        if from_suji:
            self.board[from_dan][from_suji] = PT.EMPTY.value
        else:
            self.holding[turn][piece] -= 1

        if move_info.promote:
            self.board[to_dan][to_suji] = piece + PT.PROMOTED.value 
        else:
            self.board[to_dan][to_suji] = piece

    @staticmethod
    def in_board(dan,suji):
        return (1 <= dan <= 9 and 1 <= suji <= 9)


class MoveInfo():

    def __init__(self, src, dist, piecetype, promote):
        self.src = src
        self.dist = dist
        self.piecetype = piecetype
        self.promote = promote

    def show(self):
        if self.src[0] != 0:
            print("{}{}".format(self.src[0], self.src[1]), end="")
        print("{}{}".format(self.dist[0], self.dist[1]), end="")
        print("{}".format(Position.PIECE_STR[self.piecetype.value]), end="")
        if self.src[0] == 0:
            print("打  ")
        elif self.promote:
            print("成")
        else:
            print("  ")