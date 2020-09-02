from unittest import TestCase
# import sys
# sys.path.append("..")
from eggplant import position

class TestPosition(TestCase):
    
    # def test_show(self):
    #     # p = position.Position()
    #     p = position.Position()
    #     p.show()

    def test_initialize_board(self):
        p = position.Position()
        p.initialize_board()
        p.show()


    # def test_clear_board(self):
