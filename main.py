from controller.player_controller import PlayerController
from controller.board_controller import BoardController
from controller.game_controller import GameController

if __name__ == "__main__":
    player1_input = input("create player by entering piece followed by name: ")
    player2_input = input("create player by entering piece followed by name: ")
    player_controller = PlayerController()
    game_controller = GameController()
    board_controller = BoardController()
    player1 = player_controller.create_player(player1_input.split(" ")[1], player1_input.split(" ")[0])
    game_controller.initialize_players(player1)
    player2 = player_controller.create_player(player2_input.split(" ")[1], player2_input.split(" ")[0])
    game_controller.initialize_players(player2)
    board = board_controller.create_board(3)
    game_controller.initialize_board(board)
    game_controller.start_game()
