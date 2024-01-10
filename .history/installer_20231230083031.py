import tkinter as tk
window = tk.Tk()

window.title("Installer")

# Setup the window ( Install button and add Kip to the path checkbox )

install = tk.Button(window, text="Install", command=window.destroy)

install.pack(side=tk.BOTTOM, fill=tk.X)

window.mainloop()
