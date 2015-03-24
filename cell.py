import weakref

class Cell(object):
    def __init__(self, board, index):
        self.index = index
        self.board = weakref.ref(board)

    # Would be nice to have all of this for all of the cell objects
    # maybe a mixin is in order

    def up(self):
        pass

    def down(self):
        pass

    def left(self):
        pass

    def right(self):
        pass

    def upper_left(self):
        pass

    def upper_right(self):
        pass

    def lower_left(self):
        pass

    def lower_right(self):
        pass

    def row(self):
        pass

    def column(self):
        pass

    def move(self):
        pass

    def delete(self):
        pass