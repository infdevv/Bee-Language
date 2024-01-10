import tkinter as tk
from tkinter import ttk
import subprocess
window = tk.Tk()

window.title("Installer")

# Setup the window ( Install button and add Kip to the path checkbox )

# Make it run a batch script when install is clicked, then clear the window and display the finished installing message

install = tk.Button(window, text="Install", command=lambda: installer())

add_kip = tk.Checkbutton(window, text="Add Kip to path", command=lambda: subprocess.run("installer\\add_kip.bat"))

add_kip.pack(side=tk.LEFT, fill=tk.X)

install.pack(side=tk.BOTTOM, fill=tk.X)

# Set window size

window.geometry("300x200")

# Once install is clicked, clear the window and display the finished installing message

def installer():

    progressbar = ttk.Progressbar(mode="indeterminate")
    progressbar.place(x=30, y=60, width=200)
    # Start moving the indeterminate progress bar.
    progressbar.start()
    window.geometry("300x200")
    window.mainloop()



    subprocess.run("installer\\installer.bat")
    # Clear the window
    for widget in window.winfo_children():
        widget.destroy()

    # Display the finished installing message
    tk.Label(window, text="Finished installing!").pack()
    leave = tk.Button(window, text="Leave", command=lambda: window.destroy())

    leave.pack()

window.mainloop()
