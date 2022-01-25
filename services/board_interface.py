import abc


class BoardInterface(metaclass=abc.ABCMeta):
    """
    BoardInterface
    """
    @abc.abstractmethod
    def create_board(self, board_size):
        pass
