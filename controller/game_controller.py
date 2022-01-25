from services.game_service import GameServices


class GameController:
    """
        GameController: This class represents the game controller
    """
    def __init__(self):
        self.game_service = GameServices()

    def initialize_players(self, player):
        """
        This method is used to initialize player to the game using game service
        :param player: Player
        """
        self.game_service.initialize_players(player)

    def initialize_board(self, board):
        """
        This method is used to initialize board to the game using board service
        :param board: Board
        """
        self.game_service.initialize_board(board)

    def start_game(self):
        """
        This method is used to start the game using game service
        """
        self.game_service.start()
