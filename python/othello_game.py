class OthelloGame:
    def __init__(self):
        self.board = [[" " for _ in range(8)] for _ in range(8)]
        self.current_player = "B"  # B for Black, W for White
        self.initialize_board()

    def initialize_board(self):
        # Set up the initial 4 pieces in the center
        self.board[3][3] = "W"
        self.board[3][4] = "B"
        self.board[4][3] = "B"
        self.board[4][4] = "W"

    def print_board(self):
        print("  A B C D E F G H")
        for i, row in enumerate(self.board):
            print(f"{i+1} " + " ".join(row))

    def is_valid_move(self, row, col):
        # Check if the move is within bounds and the cell is empty
        if row < 0 or row >= 8 or col < 0 or col >= 8 or self.board[row][col] != " ":
            return False
        # Additional logic to check if the move flips opponent's pieces
        return True

    def make_move(self, row, col):
        if not self.is_valid_move(row, col):
            print("Invalid move. Try again.")
            return False

        self.board[row][col] = self.current_player
        # Logic to flip opponent's pieces
        self.flip_pieces(row, col)
        self.current_player = "W" if self.current_player == "B" else "B"
        return True

    def flip_pieces(self, row, col):
        # Placeholder for flipping logic
        pass

    def has_valid_moves(self):
        for row in range(8):
            for col in range(8):
                if self.is_valid_move(row, col):
                    return True
        return False

    def play_game(self):
        while self.has_valid_moves():
            self.print_board()
            print(f"{self.current_player}'s turn.")
            move = input("Enter your move (e.g., D3): ")
            if len(move) != 2 or move[0] not in "ABCDEFGH" or not move[1].isdigit():
                print("Invalid input. Use the format 'D3'.")
                continue

            col = ord(move[0].upper()) - ord("A")
            row = int(move[1]) - 1

            if not self.make_move(row, col):
                continue

        print("Game over!")
        self.print_board()

if __name__ == "__main__":
    print("Starting Othello Game...")
    game = OthelloGame()
    game.play_game()