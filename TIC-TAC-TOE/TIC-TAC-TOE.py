import tkinter as tk
import tkinter.messagebox
import random

# Initialize the board
board = [" " for _ in range(9)]
current_player = "X"
game_over = False

# Create the GUI
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Function to check for a win
def check_win(player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]

    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            draw_winning_line(combo)  # Draw the winning line
            return True
    return False

# Function to draw the winning line
def draw_winning_line(combo):
    x1, y1 = (combo[0] % 3) * 100 + 50, (combo[0] // 3) * 100 + 50
    x2, y2 = (combo[2] % 3) * 100 + 50, (combo[2] // 3) * 100 + 50
    canvas.create_line(x1, y1, x2, y2, fill="red", width=5)

# Function to check for a draw
def check_draw():
    return " " not in board

# Function to handle player's move
def player_move(index):
    global current_player, game_over
    if board[index] == " " and not game_over:
        board[index] = current_player
        update_board()
        if check_win(current_player):
            tk.messagebox.showinfo("Tic-Tac-Toe", f"Player {current_player} wins!")
            game_over = True
        elif check_draw():
            tk.messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            game_over = True
        else:
            current_player = "O"
            ai_move()

# Function to update the GUI with the current board state
def update_board():
    for i in range(9):
        if board[i] != " ":
            x, y = (i % 3) * 100 + 50, (i // 3) * 100 + 50
            canvas.create_text(x, y, text=board[i], font=("Arial", 60))

# AI's move (randomly selects an empty cell)
def ai_move():
    global current_player, game_over
    if not game_over:
        empty_cells = [i for i in range(9) if board[i] == " "]
        if empty_cells:
            ai_choice = random.choice(empty_cells)
            board[ai_choice] = "O"
            update_board()
            if check_win("O"):
                tk.messagebox.showinfo("Tic-Tac-Toe", "AI wins!")
                game_over = True
            elif check_draw():
                tk.messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                game_over = True
            else:
                current_player = "X"

# Create the game board
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()

canvas.create_line(100, 0, 100, 300, fill="black", width=3)
canvas.create_line(200, 0, 200, 300, fill="black", width=3)
canvas.create_line(0, 100, 300, 100, fill="black", width=3)
canvas.create_line(0, 200, 300, 200, fill="black", width=3)

canvas.bind("<Button-1>", lambda event: player_move((event.y // 100) * 3 + (event.x // 100)))

# Start the game
root.mainloop()
