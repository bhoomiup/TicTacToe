from models.game import Game


class GameServices:
    """
    GameServices: This class contains all the logical implementations of the game
    """

    def __init__(self):
        self.game = Game()
        self.exit_game = False
        self.match_draw = False
        self.count = 0

    def initialize_players(self, player):
        """
        This method is used to initialize players to game
        :param player: Player
        """
        self.game.players.append(player)
        print(f"{player.name} added to game")

    def initialize_board(self, board):
        """
        This method is used to initialize board to game
        :param board: Board
        """
        self.game.board = board
        print(f"board added to game")
        self.print_board()

    def start(self):
        """
        This method is used to start the game
        """
        while (not self.game.winner) and (not self.match_draw) and (not self.exit_game):
            for player in self.game.players:
                self.player_chance(player)
                self.count += 1
                if self.exit_game or self.match_draw:
                    break
                if self.game.winner:
                    print(f"{self.game.winner.name} won the game")
                    break

    def player_chance(self, player):
        """
        This method is used to take player input and place the piece in board accordingly
        :param player:
        :return:
        """
        # check if all positions in board are filled
        if self.check_end_game():
            print("Game Over")
            return
        cell_pos = input("Please enter the cell position: ")
        # exits game if exit is provided
        if cell_pos == "exit":
            self.exit_game = True
            return
        pos0 = int(cell_pos.split(" ")[0]) - 1
        pos1 = int(cell_pos.split(" ")[1]) - 1
        if self.game.board.board_grid[pos0][pos1] == "_":
            self.game.board.board_grid[pos0][pos1] = player.piece_assigned
            self.check_winner(player)
            self.print_board()
        else:
            print("Invalid move!")
            # providing the same player another chance if invalid input provided
            self.player_chance(player)

    def check_winner(self, player):
        """
        This method is used to check the winner of the game after every chance of player
        :param player: Player
        """
        count_dict = {"vertical_count": 0, "horizontal_count": 0, "diagonal_count": 0}
        for i in range(self.game.board.size):
            if self.game.board.board_grid[0][i] == player.piece_assigned:
                count_dict["vertical_count"] += 1
            if self.game.board.board_grid[i][0] == player.piece_assigned:
                count_dict["horizontal_count"] += 1
            if self.game.board.board_grid[i][i] == player.piece_assigned:
                count_dict["diagonal_count"] += 1

        for i in count_dict.values():
            if i == self.game.board.size:
                self.game.winner = player
                break

    def check_end_game(self):
        """
        This method is used to check if all the positions in the board is Filled.
        :return: boolean
        """
        if self.count == self.game.board.size ** 2:
            self.match_draw = True
            return self.match_draw

    def print_board(self):
        """
        This method is used to print board
        """
        for i in self.game.board.board_grid:
            print(str(i)[1:-1].replace(",", "").replace("'", ""), end="\n")
