import tkinter as tk
from tkinter import ttk
import subprocess
import os

def add_kip():
    subprocess.run("installer\\add_kip.bat")

def installer():
    # Create a Toplevel window for the progress bar
    progress_window = tk.Toplevel(window)
    progress_window.title("Installing")

    # Run ./compiler/py-compiler/get-pip.py 
    # Implementing the comment: Use os.path.join to handle file paths
    pip_script_path = os.path.join("compiler", "py-compiler", "get-pip.py")
    subprocess.run(["compiler\\py-compiler\\python.exe", pip_script_path])

    # epic logic for running ./compiler/py-compiler/get-pip.py in a method
    # so that it alters ./compiler/py-compiler and not ./

    # Add a label to show progress
    progress_label = tk.Label(progress_window, text="Installing...")
    progress_label.pack(pady=10)

    # Add a progress bar
    progressbar = ttk.Progressbar(progress_window, mode="indeterminate")
    progressbar.pack(pady=10)

    # Start moving the indeterminate progress bar.
    progressbar.start()

    # Update the window to show progress
    progress_window.update()

    # Run the installer script in a subprocess
    # Implementing the comment: Use os.path.join to handle file paths
    installer_script_path = os.path.join("installer", "installer.bat")
    subprocess.run([installer_script_path])

    # Stop the progress bar
    progressbar.stop()

    # Destroy the progress window
    progress_window.destroy()

    # Clear the main window
    for widget in window.winfo_children():
        widget.destroy()

    # Display the finished installing message
    tk.Label(window, text="Finished installing!").pack()
    leave = tk.Button(window, text="Leave", command=lambda: window.destroy())
    leave.pack()

window = tk.Tk()
window.title("Installer")

# Setup the window ( Install button and add Kip to the path checkbox )

# Make it run a batch script when install is clicked, then clear the window
# and display the finished installing message

add_kip = tk.Checkbutton(window, text="Add Kip to path", command=lambda: add_kip())
add_kip.pack(side=tk.LEFT, fill=tk.X)

install = tk.Button(window, text="Install", command=installer)
install.pack(side=tk.BOTTOM, fill=tk.X)

# Set window size
window.geometry("300x200")

window.mainloop()
