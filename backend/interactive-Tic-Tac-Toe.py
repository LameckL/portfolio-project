#!/usr/bin/env python3

import random
import math

# Class representing the Tic Tac Toe game state
class TicTacToe:
    def __init__(self):
        """
        Initializes the Tic Tac Toe game state.
        """
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.winner = None

    def make_move(self, position):
        """
        Makes a move in the game at the specified position.
        """
        if self.board[position] == " ":
            self.board[position] = self.current_player
            self.current_player = "X" if self.current_player == "O" else "O"
            self.check_winner()

    def check_winner(self):
        """
        Checks if there is a winner in the current game state.
        """
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            a, b, c = combo
            if self.board[a] == self.board[b] == self.board[c] != " ":
                self.winner = self.board[a]
                return

    def is_draw(self):
        """
        Checks if the game is a draw.
        """
        return " " not in self.board

    def is_terminal(self):
        """
        Checks if the game has reached a terminal state (draw or a player wins).
        """
        return self.is_draw() or self.winner is not None

    def get_legal_moves(self):
        """
        Returns a list of legal moves in the current game state.
        """
        return [i for i in range(9) if self.board[i] == " "]

    def copy(self):
        """
        Creates a copy of the current game state.
        """
        copied_state = TicTacToe()
        copied_state.board = self.board.copy()
        copied_state.current_player = self.current_player
        copied_state.winner = self.winner
        return copied_state

# Function to display the Tic Tac Toe board
def display_board(board):
    print("-------------")
    for i in range(3):
        row = "|"
        for j in range(3):
            row += " " + board[i * 3 + j] + " |"
        print(row)
        print("-------------")

# Function for interactive gameplay
def play_game():
    # Initialize Tic Tac Toe game
    game = TicTacToe()
    display_board(game.board)
    while not game.is_terminal():
        if game.current_player == "X":
            # Human player's turn
            while True:
                try:
                    position = int(input("Enter position (0-8): "))
                    if position not in game.get_legal_moves():
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input. Please enter a number between 0 and 8.")
            game.make_move(position)
        else:
            # AI player's turn (you can replace this with your MCTSRAVE algorithm)
            position = random.choice(game.get_legal_moves())
            game.make_move(position)
        display_board(game.board)

    # Print game result
    if game.winner:
        print("Player", game.winner, "wins!")
    else:
        print("It's a draw!")

# Play the game
play_game()
