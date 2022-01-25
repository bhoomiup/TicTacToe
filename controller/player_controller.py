from services.player_service import PlayerServices


class PlayerController:
    """
        PlayerController: This class represents the player controller
    """
    def __init__(self):
        self.player_service = PlayerServices()

    def create_player(self, name, piece_assigned):
        """
        This method is used to create a player using player service
        :param name: string
        :param piece_assigned: string
        :return: Player
        """
        player = self.player_service.create_player(name, piece_assigned)
        return player
