import tkinter as tk
from tkinter import ttk
import subprocess

def installer():
    # Create a Toplevel window for the progress bar
    progress_window = tk.Toplevel(window)
    progress_window.title("Installing")

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
    subprocess.run("installer\\installer.bat")

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

# Make it run a batch script when install is clicked, then clear the window and display the finished installing message

add_kip = tk.Checkbutton(window, text="Add Kip to path", command=lambda: subprocess.run("installer\\add_kip.bat"))
add_kip.pack(side=tk.LEFT, fill=tk.X)

install = tk.Button(window, text="Install", command=installer)
install.pack(side=tk.BOTTOM, fill=tk.X)

# Set window size
window.geometry("300x200")

window.mainloop()
