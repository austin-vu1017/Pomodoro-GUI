# Pomodoro-GUI
Creating a Pomodoro which helps track the amount of time worked and break duration. The app will notify if you've worked enough to commence break.

## Modules
- tkinter: Using the Tk(), Canvas(), PhotoImage(), and Label() classes to implement the UI setup and functionality.
- math: Primarily used for floor() to create an integer instead of float using Python's '/'

## Features
- reset_sw(): Completely resets the entire stopwatch. Timer is reset to 00:00, checks are removed, timer title is reverted to displaying "Timer", and global variables are set to its original value.
- start_sw(): Commences the timer. This will have a color coded timer that will show "work" in green, "short break" in pink, and "long break" in red. The order process of these modes is Work -> Short -> Work -> Short -> Work -> Short -> Work -> Long and then repeats the process.
- stopwatch(count): Responsible for displaying the timer and checks
