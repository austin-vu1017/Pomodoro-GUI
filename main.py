from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_text(100, 5, text="Timer", fill=GREEN, font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=1)
tomato_img = PhotoImage(file="./pomodoro-start/tomato.png")
# create_image(x, y, image). x=100 to prevent image cutoffs
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)
canvas.create_text(100, 220, text="✔", fill=GREEN)
canvas.grid(column=2, row=4)

start_label = Label(text="Start")
start_label.grid(column=1, row=3)
reset_label = Label(text="Reset")
reset_label.grid(column=3, row=3)

window.mainloop()