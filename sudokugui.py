import tkinter as tk
import sudoku

window = tk.Tk()
window.title("Sudoku Solver")
window.configure(background='black')

def run():
    sudokuBoard = list()
    for row in squares:
        r = list()
        for j in row:
            if not j.get() == "":
                try:
                    r.append(int(j.get()))
                except:
                    print("not int")
                    exit
            else:
                r.append(0)
        sudokuBoard.append(r)
    result = sudoku.solveSudoku(sudokuBoard)
    for key in result:
        squares[key[0]][key[1]].delete(0, tk.END)
        squares[key[0]][key[1]].insert(0, result[key])


squares = list()
for i in range(9):
    rowsquares = list()
    for j in range(9):
        RC = tk.Entry(window, width = 5)
        RC.grid(row = i, column = j, sticky='W')
        rowsquares.append(RC)
    squares.append(rowsquares)

tk.Button(window, text="run", width = 3, command=run).grid(row = 9, sticky='W')


window.mainloop()