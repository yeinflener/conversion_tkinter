import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    print(entry_int.get())
    output_string.set(km_output)

# Define a window - window is the root of your application, or the simplest
# form of your app: blank window to work with, like add a login app
# if you don't have window, there's no place to place all of your stuff, can't
# have buttons like floating in the air, so need a window

window = ttk.Window(themename = "journal")
window.title("Demo")
window.geometry("300x150")
# window.configure(background="#333333")
# title
title_label = ttk.Label(master= window, text="Miles to kilometers", font = "Arial 24 bold")
title_label.pack()

#input field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, width=50, textvariable=entry_int)
button = ttk.Button(master = input_frame, text = "Convert", command=convert)
entry.pack(side = "left", padx = 6)
button.pack(side = "right")
button.pack()
input_frame.pack(pady = 10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(master=window, text="Output", font = "Arial 18", textvariable=output_string)
output_label.pack(pady = 5)

# run
window.mainloop()

# Tutorial on tkinter by Atlas