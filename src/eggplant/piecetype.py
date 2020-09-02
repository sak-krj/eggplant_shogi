from enum import Enum

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

def is_self(piece):
    return PieceType.FU <= piece and piece <= PieceType.RY

def is_enemy(piece):
    return piece & PieceType.ENEMY