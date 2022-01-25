from models.player import Player


class PlayerServices:
    """
    PlayerServices: This class contains all the logical implementations for player
    """

    def create_player(self, name, piece_assigned):
        """
        This method is used to create player
        :param name: string
        :param piece_assigned: string
        :return: Player
        """
        player = Player()
        player.name = name
        player.piece_assigned = piece_assigned
        return player
