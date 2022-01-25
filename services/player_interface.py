import abc


class PlayerInterface(metaclass=abc.ABCMeta):
    """
    PlayerInterface
    """
    @abc.abstractmethod
    def create_player(self, name):
        pass
