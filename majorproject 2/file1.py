import tkinter as tk
import threading
from tkinter import ttk

def long_running_task():
    # This is the long running task that will be run in a separate thread


def start_task():
    # This function will be called when the user clicks the "Start Task" button
    progress_bar.start()
    # Start the long running task in a separate thread
    task_thread = threading.Thread(target=long_running_task)
    task_thread.start()
    # Poll the thread every 100 milliseconds to see if it has finished
    goo.after(100, check_task, task_thread)

def check_task(task_thread):
    # This function checks if the task has finished
    if task_thread.is_alive():
        # If the task is still running, poll again after 100 milliseconds
        goo.after(100, check_task, task_thread)
    else:
        # If the task has finished, stop the progress bar
        progress_bar.stop()

# Create the GUI
goo = tk.Tk()
goo.geometry("300x100")

# Create the progress bar
progress_bar = ttk.Progressbar(goo, orient="horizontal", length=200, mode="indeterminate")

# Create the "Start Task" button
start_button = tk.Button(goo, text="Start Task", command=start_task)

# Pack the progress bar and the button
progress_bar.pack(pady=10)
start_button.pack()

# Start the GUI main loop
goo.mainloop()




