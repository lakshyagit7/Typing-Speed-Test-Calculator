import tkinter as tk
from tkinter import messagebox
import random
from time import time

# Function to calculate typing mistakes
def mistake(partest, usertest):
    partest_words = partest.split()
    usertest_words = usertest.split()
    error = 0
    min_length = min(len(partest_words), len(usertest_words))
    for i in range(min_length):
        if partest_words[i] != usertest_words[i]:
            error += 1
    error += abs(len(partest_words) - len(usertest_words))
    return error

# Function to calculate typing speed
def speed_time(start_time, end_time, userinput):
    time_delay = end_time - start_time
    speed = len(userinput) / time_delay
    return round(speed, 2)

# Function to start the typing test
def start_test():
    global start_time, test1
    test = [
        "The science and engineering of making intelligent machines, especially intelligent computer programs.",
        "A computer program with AI can answer the generic questions it is meant to solve.",
        "Artificial Intelligence is a developmental science.",
        "Robot is an electromechanical technology.",
        "Democracy is a political system.",
        "Guitar is a musical instrument.",
        "Solar energy is a renewable resource.",
        "Psychology is a study of the human mind.",
        "The Great Wall of China is a historical landmark.",
        "Ice cream is a popular dessert.",
        "Internet is a global network of computers.",
        "Hiking is a recreational activity.",
        "Pizza is a beloved Italian dish.",
        "Language is a means of communication."
    ]
    test1 = random.choice(test)
    label.config(text=test1)
    entry.delete(0, tk.END)
    entry.focus()
    start_time = time()
    start_button['state'] = tk.DISABLED

# Function to end the typing test
def end_test():
    end_time = time()
    user_input = entry.get()
    typing_speed = speed_time(start_time, end_time, user_input)
    errors = mistake(test1, user_input)
    result = f"Typing Speed: {typing_speed} w/sec\nErrors: {errors}"
    messagebox.showinfo("Test Result", result)
    start_button['state'] = tk.NORMAL

# Create the GUI
root = tk.Tk()
root.geometry('940x735+200+10')
root.title("Typing Speed Test")

# Main Frame
mainframe = tk.Frame(root, bd=4)
mainframe.grid()

# Title Frame
titleframe = tk.Frame(mainframe, bg='pink')
titleframe.grid()

titleLabel = tk.Label(
    titleframe,
    text='TYPING TYCOON',
    font=('algerian', 28, 'bold'),
    bg='BLACK',
    fg='white',
    width=48,
    bd=10
)
titleLabel.grid(pady=5)

# Display random text
label = tk.Label(root, text="", font=("Helvetica", 22))
label.grid(pady=20)

# Entry widget for user input
entry = tk.Entry(root, font=("Helvetica", 24), width=50, bd=2, fg='black')
entry.grid(pady=20)

# Buttons frame
button_s = tk.Frame(root, bd=4)
button_s.grid()

# Buttons
start_button = tk.Button(button_s, text="Start Test", command=start_test, font=("Helvetica", 14), width=10, height=1)
start_button.grid(row=0, column=0)

submit_button = tk.Button(button_s, text="Submit", command=end_test, font=("Helvetica", 14), width=10, height=1)
submit_button.grid(row=0, column=1, padx=20)

exit_button = tk.Button(button_s, text="Exit", command=root.destroy, font=("Helvetica", 14), width=10, height=1)
exit_button.grid(row=0, column=2)

# Run the GUI
root.mainloop()
