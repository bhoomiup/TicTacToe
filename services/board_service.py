from models.board import Board


class BoardServices:
    """
    BoardServices: This class contains all the logical implementations for Board
    """
    def create_board(self, board_size):
        """
        This method is used to create the board using the input provided as order of the board
        :param board_size: int
        :return: Board
        """
        board = Board()
        board.size = board_size
        # creating 2-D array
        board.board_grid = [["_" for i in range(board.size)] for j in range(board.size)]
        return board
