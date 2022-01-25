class Game:
    """
    Game: This class represents the Game entity
    """
    def __init__(self):
        self._pieces = ["X", "O"]
        self._board = None
        self._players = []
        self._winner = None

    @property
    def pieces(self):
        """
        This method returns the pieces in the game
        :return: array
        """
        return self._pieces

    @property
    def board(self):
        """
        This method returns the board in the game
        :return: Board
        """
        return self._board

    @property
    def players(self):
        """
        This method returns the players in the game
        :return: Player[]
        """
        return self._players

    @property
    def winner(self):
        """
        This method returns the winner of the game
        :return: Player
        """
        return self._winner

    @pieces.setter
    def pieces(self, pieces):
        self._pieces = pieces

    @board.setter
    def board(self, board):
        self._board = board

    @players.setter
    def players(self, players):
        self._players = players

    @winner.setter
    def winner(self, winner):
        self._winner = winner

