from eggplant.position import Position
from eggplant.move import Move
from eggplant.piecetype import PieceType as PT
from eggplant.types import Types

def manual():

    p = Position()
    p.show()

    turn = 0
    while True:
        print("入力例:7 7 7 6 FU 0 [移動前の筋 段 移動後の筋 段 駒の種類 成]")
        cmds = input().split()
        if cmds[0] == "end":
            return

        src = tuple(map(int, cmds[0:2]))
        dist = tuple(map(int, cmds[2:4]))
        color = turn%2
        m = Move(src, dist, PT.string_of(cmds[4], color), int(cmds[5]), color)
        m.show()

        p.move(m)
        p.show()
        turn += 1