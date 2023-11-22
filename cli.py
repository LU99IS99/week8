from logic import TicTacToeGame

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def get_move():
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))
    return row, col

def main():
    game = TicTacToeGame()

    while True:
        print_board(game.board)
        row, col = get_move()

        if not game.make_move(row, col):
            print("Invalid move, try again.")
            continue

        if game.check_winner():
            print(f"Player {game.current_player} wins!")
            break
        elif game.is_draw():
            print("It's a draw!")
            break

    print("Game Over")

if __name__ == "__main__":
    main()
