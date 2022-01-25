class Player:
    """
    Player: This class represents the player entity
    """
    def __init__(self):
        self._name = None
        self._piece_assigned = None

    @property
    def name(self):
        """
        This method returns the name of the player
        :return: string
        """
        return self._name

    @property
    def piece_assigned(self):
        """
        This method returns the piece assigned to the player
        :return: string
        """
        return self._piece_assigned

    @name.setter
    def name(self, name):
        self._name = name

    @piece_assigned.setter
    def piece_assigned(self, piece_assigned):
        self._piece_assigned = piece_assigned
