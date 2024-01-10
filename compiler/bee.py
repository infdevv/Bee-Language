import sys
import os
import subprocess

# Ensure 'temp' directory exists
os.makedirs("temp", exist_ok=True)

# If a sys arg is provided, run it in the compiler; else, start the shell
if len(sys.argv) > 1:
    # Call subprocess using py-compiler\python.exe index.py (sys arg)
    subprocess.run([fr"py-compiler\python.exe", "index.py", sys.argv[1]])
else:
    print("Bee# Shell ( V1.3.1 ) ")
    while True:
        data = input("> ")

        if data == "exit":
            break

        with open(os.path.join("temp", "doc.txt"), "w+") as f:
            f.write(data)

        subprocess.run([fr"py-compiler\python.exe", "index.py", os.path.join("temp", "doc.txt")])

        os.remove(os.path.join("temp", "doc.txt"))
