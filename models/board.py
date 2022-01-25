class Board:
    """
    Board: This class represents the board entity
    """
    def __init__(self):
        self._size = 3
        self._board_grid = None

    @property
    def size(self):
        """
        This method returns order of the board
        :return: int
        """
        return self._size

    @property
    def board_grid(self):
        """
        This method returns board grid
        :return: array
        """
        return self._board_grid

    @size.setter
    def size(self, size):
        self._size = size

    @board_grid.setter
    def board_grid(self, board_grid):
        self._board_grid = board_grid
