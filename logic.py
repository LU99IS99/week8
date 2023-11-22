class TicTacToeGame:
    def __init__(self):
        self.board = [['', '', ''], ['', '', ''], ['', '', '']]
        self.current_player = 'X'  # 'X' starts the game

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def make_move(self, row, col):
        if self.board[row][col] == '':
            self.board[row][col] = self.current_player
            self.switch_player()
            return True
        return False

    def check_winner(self):
        # Logic to check for a winner or a draw
        pass

    def is_draw(self):
        # Logic to check if the game is a draw
        pass

    def reset_game(self):
        self.board = [['', '', ''], ['', '', ''], ['', '', '']]
        self.current_player = 'X'
