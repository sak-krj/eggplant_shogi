from enum import Enum
from eggplant.types import Types

class PieceType(Enum):
    OUT_OF_BOARD = 64
    PROMOTED = 8
    ENEMY = 16
    EMPTY  = 0
    FU = 1
    KY = 2
    KE = 3
    GI = 4
    KI = 5
    KA = 6
    HI = 7
    OU = 8
    TO = PROMOTED + FU
    NY = PROMOTED + KY
    NK = PROMOTED + KE
    NG = PROMOTED + GI
    UM = PROMOTED + KA
    RY = PROMOTED + HI
    EFU = ENEMY + FU
    EKY = ENEMY + KY
    EKE = ENEMY + KE
    EGI = ENEMY + GI
    EKI = ENEMY + KI
    EKA = ENEMY + KA
    EHI = ENEMY + HI
    EOU = ENEMY + OU
    ETO = ENEMY + TO
    ENY = ENEMY + NY
    ENK = ENEMY + NK
    ENG = ENEMY + NG
    EUM = ENEMY + UM
    ERY = ENEMY + RY

    @classmethod
    def is_self(self, piece):
        return PieceType.FU <= piece and piece <= PieceType.RY

    @classmethod
    def is_enemy(self, piece):
        return piece & PieceType.ENEMY

    @classmethod
    def is_promoted(self, piece):
        return (PieceType.TO.value <= piece <= PieceType.RY.value or PieceType.ETO.value <= piece <= PieceType.ERY.value)

    @classmethod
    def value_of(self, val):
        for e in PieceType:
            if val == e.value:
                return e

    @classmethod
    def string_of(self, s, color):
        val = Types.PIECE＿CSA.index(s) + color * PieceType.ENEMY.value
        return PieceType.value_of(val)