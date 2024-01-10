import tkinter as tk
import subprocess
window = tk.Tk()

window.title("Installer")

# Setup the window ( Install button and add Kip to the path checkbox )

# Make it run a batch script when install is clicked, then clear the window and display the finished installing message

install = tk.Button(window, text="Install", command=lambda: subprocess.run("installer.bat"))

add_kip = tk.Checkbutton(window, text="Add Kip to path", command=lambda: subprocess.run("add_kip.bat"))

add_kip.pack(side=tk.LEFT, fill=tk.X)

install.pack(side=tk.BOTTOM, fill=tk.X)

window.mainloop()
