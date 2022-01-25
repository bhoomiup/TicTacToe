from services.board_service import BoardServices


class BoardController:
    """
        BoardController: This class represents the board controller
    """
    def __init__(self):
        self.board_service = BoardServices()

    def create_board(self, board_size):
        """
        This method is used to create board by calling board service
        :param board_size: int
        :return: Board
        """
        board = self.board_service.create_board(board_size)
        return board
