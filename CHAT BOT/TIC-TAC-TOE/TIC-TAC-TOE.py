import tkinter as tk
import tkinter.messagebox

# Initialize the board
board = [" " for _ in range(9)]
current_player = "X"
game_over = False

# Function to check for a win
def check_win():
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != " ":
            canvas.create_line(i * 100 + 50, 15, i * 100 + 50, 285, fill="red", width=5)
            return True
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != " ":
            canvas.create_line(15, i * 100 + 50, 285, i * 100 + 50, fill="red", width=5)
            return True
    if board[0] == board[4] == board[8] != " ":
        canvas.create_line(15, 15, 285, 285, fill="red", width=5)
        return True
    if board[2] == board[4] == board[6] != " ":
        canvas.create_line(15, 285, 285, 15, fill="red", width=5)
        return True
    return False

# Function to check for a draw
def check_draw():
    return " " not in board

 
def player_move(index):
    global current_player, game_over
    if board[index] == " " and not game_over:
        board[index] = current_player
        draw_move(index)
        if check_win():
            tk.messagebox.showinfo("Tic-Tac-Toe", f"Player {current_player} wins!")
            game_over = True
        elif check_draw():
            tk.messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            game_over = True
        else:
            current_player = "O"
            ai_move()

 
def draw_move(index):
    x, y = (index % 3) * 100 + 50, (index // 3) * 100 + 50
    canvas.create_text(x, y, text=current_player, font=("Arial", 60))

 
def minimax(board, depth, maximizing_player):
    if check_win():
        return -1 if maximizing_player else 1
    elif check_draw():
        return 0

    if maximizing_player:
        max_eval = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                eval = minimax(board, depth + 1, False)
                board[i] = " "
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                eval = minimax(board, depth + 1, True)
                board[i] = " "
                min_eval = min(min_eval, eval)
        return min_eval

 
def ai_move():
    global current_player
    if not game_over:
        best_move = None
        best_eval = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                move_eval = minimax(board, 0, False)
                board[i] = " "
                if move_eval > best_eval:
                    best_eval = move_eval
                    best_move = i
        if best_move is not None:
            board[best_move] = "O"
            draw_move(best_move)
            if check_win():
                tk.messagebox.showinfo("Tic-Tac-Toe", "AI wins!")
                game_over = True
            elif check_draw():
                tk.messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                game_over = True
            else:
                current_player = "X"
 
root = tk.Tk()
root.title("Tic-Tac-Toe")

canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()

canvas.create_line(100, 0, 100, 300, fill="black", width=3)
canvas.create_line(200, 0, 200, 300, fill="black", width=3)
canvas.create_line(0, 100, 300, 100, fill="black", width=3)
canvas.create_line(0, 200, 300, 200, fill="black", width=3)

canvas.bind("<Button-1>", lambda event: player_move((event.y // 100) * 3 + (event.x // 100)))

# Start the game
root.mainloop()
