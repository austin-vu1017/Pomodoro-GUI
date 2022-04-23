from tkinter import *
import math


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
        
def reset_sw():
    global reps 
    
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(stopwatch_text, text="00:00")
    check_label.config(text="")
    reps = 0

def start_sw():
    global reps 
    reps += 1

    if reps == 8:
        timer_label.config(text="Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
        stopwatch(LONG_BREAK_MIN)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
        stopwatch(SHORT_BREAK_MIN)
    else:
        timer_label.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
        stopwatch(WORK_MIN)

def stopwatch(count):
    global reps
    minute = math.floor(count / 60)
    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"   
    canvas.itemconfig(stopwatch_text, text=f"{minute}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, stopwatch, count - 1)
    else:
        start_sw()
        checkmarks = ""
        for i in range(math.floor(reps / 2)):
            checkmarks += "✔"
        check_label.config(text=checkmarks)

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./pomodoro-start/tomato.png")
# create_image(x, y, image). x=100 to prevent image cutoffs
canvas.create_image(100, 112, image=tomato_img)
stopwatch_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

# Labels
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=2, row=1)
check_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
check_label.grid(column=2, row=4)

# Buttons
start_button = Button(text="Start", command=start_sw)
start_button.grid(column=1, row=3)
reset_button = Button(text="Reset", command=reset_sw)
reset_button.grid(column=3, row=3)

window.mainloop()