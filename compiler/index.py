import sys
import os
import subprocess
import asyncio
import random
from pathlib import Path
from time import sleep
import tkinter as tk
from tkinter import ttk
import subprocess
import os
import requests
import sys
import os
import subprocess
import atexit

# on exit delete ./file_program.py from existance
atexit.register(lambda: os.remove("file_program.py"))


"""

version=1.4 


Bee# Compiler

"""





def main_init_live_terminal_end():
    with open("live_trm/live_terminal.txt", "w+") as f:
        f.write("+-end_stream-+")


def main_init_live_terminal_end():
    with open("live_trm/live_terminal.txt", "w+") as f:
        f.write("+-end_stream-+")

def main_init_live_terminal():
    # Run the live terminal in a new window
    subprocess.Popen(["python", "live_terminal.py"], creationflags=subprocess.CREATE_NEW_CONSOLE, shell=True)

def main_init_live_terminal_write(content):
    with open("live_trm/live_terminal.txt", "w+") as f:
        f.write(content)    

def main_init_super_variable_function(variable):
    name_var = variable[1:3]
    with open(f"super_var/{name_var}.txt", "w+") as f:
        f.write(variable)

def main_init_super_variable_function_read(variable):
    name_var = variable[1:3]
    with open(f"super_var/{name_var}.txt", "r") as f:
        return f.read()


# Other functions remain unchanged...


def main_init_cleanup_super_variable():
    print("")   

def compiler(string):

    variable_types = ["int", "float", "str", "bool"] # " This is a surprise tool that will help us later " - Mickey Mouse 

    invalid_terms=["main_init_live_terminal","main_init_live_terminal_write", "main_init_live_terminal_clear", "main_init_live_terminal_end", "main_init_transfer_javascript","main_init_super_variable_function", "main_init_super_variable_function_read", "main_init_cleanup_super_variable", "main_init_write_file", "main_init_read_file", "main_init_javascript_runner"]

    for term in invalid_terms:
        if term in string:
            raise SyntaxError(f"Unallowed term {term}. This term is reserved for the compiler.")

    string = string.replace("//", "#")
    string = string.replace("live.terminal.start", "main_init_live_terminal")
    string = string.replace("live.terminal.write","main_init_live_terminal_write")
    string = string.replace("live.terminal.clear", "main_init_live_terminal_clear")
    string = string.replace("live.terminal.end", "main_init_live_terminal_end")
    string = string.replace("file.write", "main_init_write_file")
    string = string.replace("file.read", "main_init_read_file")
    string = string.replace("doc.log", "print")
    string = string.replace("doc.error", "raise ValueError")
    string = string.replace("svar", "main_init_super_variable_function")
    string = string.replace("svar_read", "main_init_super_variable_function_read")
    string = string.replace("end()", "main_init_cleanup_super_variable()")
    
    new_string = string.split("\n")
    new = []
    expected = 0
    exit = 1
    doc1 = ""
    
    for line in new_string:
        if line == new_string[-1]:
            if line ==("main_init_cleanup_super_variable()"):
                exit = 1
                break
            else:
                exit=1
                #raise ValueError("Syntax error: Script not closed properly, cleanup not finished")

        if line.startswith("const"):
         parts = line.split(" ")
         variable_name = parts[1].strip()  # Strip to remove any leading/trailing spaces

         for other_line in new_string:
            if other_line != line and variable_name in other_line:
                raise SyntaxError("A constant variable '{}' CANNOT be altered.".format(variable_name))



        if line.startswith("function"):
            line = line.replace("function", "def")

        if line.startswith("#include"):
         
         path = "site_packages"

         try:
           
           # open com.bat on line.replace("#include ", "")+".py" in subprocess

            script_dir = os.path.dirname(os.path.abspath(__file__))
            file_name = line.replace("#include ", "").strip() + ".py"
            file_path = os.path.abspath(os.path.join(script_dir, "site_packages", file_name))
            if os.path.exists(file_path):
                with open(file_path, "r") as f:
                
                            
                    doc1=doc1+"\n"+(f.read())



            # Now brutally fuck the file up, aka delete it    

         except FileNotFoundError:
            raise ModuleNotFoundError(f"Module {line.replace('#include ', '')} was not found.")
         except Exception as e:
             raise SyntaxError(f"Error executing module {line.replace('#include ', '')}: {str(e)}")
        
        
        
        if line.endswith("{"):
            line = line[:-1] + ":"
            expected += 1
        
        if line.replace(" ","").endswith("}"):
            expected -= 1
            line=line.replace("}", "")

        for item in variable_types:
            if line.startswith(item):
                # Do a lil thing known as: if its not defined as anything in it such as: " int a " then we will define it for them
                # check if = is in the line
                if "=" not in line:
                    types={
                        "int": "int(0)",
                        "float": "float(0.0)",
                        "str": 'str("")',
                        "bool": False
                    }

                    line=line+"="+str(types[item])
                    line=line.replace(" ", "")
                elif item != "str":
                    line=line.replace(" ", "")    
                line=line.replace(item, "")


        new.append(line)

    code = "\n".join(new)

    if expected != 0:
        print("Syntax error: Function not closed")
        return

    
    
    #print("\n".join(new))
    
    code = "\n".join(new)
    file_name = "file_program.py"
    # Get the current working directory
    cwd = os.getcwd()
    compiler_path = r"python"
    # Get the directory of the current script
    script_directory = os.path.dirname(os.path.abspath(__file__))
    # Set the working directory to the script's directory
    os.chdir(script_directory)
    # Use a with statement for the file handling
    with open(file_name, "w+") as f:
        f.write(f"{doc1}\n{code}")
    subprocess.Popen([compiler_path, file_name]).wait()
    os.remove(file_name)
    
    if exit == 1:
        main_init_cleanup_super_variable()



def compile_bee_file(input_file):
    with open(input_file, "r") as f:
        string = f.read()
        compiler(string)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: index.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    # Check if the input_file exists as a file
    if os.path.isfile(input_file):
        with open(input_file, 'r') as file:
            input_data = file.read()

        # Call the function to compile the input data
        compile_bee_file(input_file)
    else:
        # Treat input_file as plain text
        input_data = input_file

        # Call the function to compile the input data
        compile(input_data)
        sys.exit(1)
