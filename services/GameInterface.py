import abc


class GameInterface(metaclass=abc.ABCMeta):
    """
    GameInterface
    """
    @abc.abstractmethod
    def move(self, player, position):
        pass

    @abc.abstractmethod
    def initialize_players(self, player):
        pass

    @abc.abstractmethod
    def initialize_board(self, board):
        pass

    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def player_chance(self, player):
        pass

    @abc.abstractmethod
    def check_winner(self, player):
        pass
