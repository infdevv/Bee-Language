import sys
import os
import subprocess
import asyncio
import random

"""

Bee# Compiler

bee# will be the first language to be a super set of a lanngugage yet stil be able to run another language

"""

def main_init_live_terminal_end():
    with open("live_trm/live_terminal.txt", "w+") as f:
        f.write("+-end_stream-+")

def main_init_live_terminal():
    # Run the live terminal in a new window
    subprocess.Popen(["python", "live_terminal.py"], creationflags=subprocess.CREATE_NEW_CONSOLE, shell=True)

def main_init_live_terminal_write(content):
    with open("live_trm/live_terminal.txt", "w+") as f:
        f.write(content)

def main_init_live_terminal_clear():
    with open("live_trm/live_terminal.txt", "w+") as f:
        f.write("-+clear+-")        

def main_init_super_variable_function(variable):
    name_var = variable[1:3]
    with open(f"super_var/{name_var}.txt", "w+") as f:
        f.write(variable)

def main_init_super_variable_function_read(variable):
    name_var = variable[1:3]
    with open(f"super_var/{name_var}.txt", "r") as f:
        return f.read()

def main_init_cleanup_super_variable():
    folder_path = "super_var"
    
    if os.path.exists(folder_path):
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            os.remove(file_path)
    else:
        print("Folder not found.")

    folder_path = "temp"
    
    if os.path.exists(folder_path):
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            os.remove(file_path)
    else:
        print("Folder not found.")    

    folder_path = "live_trm"
    
    if os.path.exists(folder_path):
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            os.remove(file_path)
    else:
        print("Folder not found.")    

def main_init_write_file(file, content, method):
    with open(file, method) as f:
        f.write(content)

def main_init_read_file(file):
    with open(file, "r") as f:
        return f.read()
 
def main_init_transfer_javascript(code):

    # Generate a random name for the file
    random_name = str(random.randint(100000, 999999))

    with open(f"temp/{random_name}.js", "w") as f:
        f.write(code)


    # So, what this function does is transfer the code process from python/bee# to javascript

    # Check if node.js is installed

    try:
        subprocess.run(["node", "--version"], check=True)
    except subprocess.CalledProcessError:
        raise SyntaxError("Error: Node.js is not installed or not available. Please install Node.js and try again.")

    # Run js_runner.js
    
    # We must launch it without subprocess as for we are going to kill the bee#/python script directly after

    # Open the js_runner.js file
    
    with open("temp/js_data.txt", "w+") as f:
        f.write(code)

    open(f"js_runner.js")

    # Commit die on this script

    print("Swapped to javascript")
    quit()


def main_init_javascript_runner(code, runtime):
    # Check if runtime is defined
    if not runtime:
        print("No runtime specified. Automatically setting runtime to 1000ms")
        runtime = 1000
    
    try:
        subprocess.run(["node", "--version"], check=True)
    except subprocess.CalledProcessError:
        raise SyntaxError("Error: Node.js is not installed or not available. Please install Node.js and try again.")
    
    # Generate a random name for the file
    random_name = str(random.randint(100000, 999999))

    with open(f"temp/{random_name}.js", "w") as f:
        f.write(code)

    try:
        # Run the Node.js script
        subprocess.run(["node", f"temp/{random_name}.js"], timeout=runtime / 1000)
    except subprocess.TimeoutExpired:
        # If the script exceeds the specified runtime, kill the process
        if os.name == "nt":
            subprocess.run(["taskkill", "/f", "/im", "node.exe"])
        else:
            subprocess.run(["pkill", "node"])
    finally:
        # Asyncio sleep is unnecessary here
        # Cleanup: Remove the temporary JavaScript file
        os.remove(f"temp/{random_name}.js")
            
def compiler(string):

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
    string = string.replace("javascript_exec","main_init_javascript_runner")
    string = string.replace("svar", "main_init_super_variable_function")
    string = string.replace("svar_read", "main_init_super_variable_function_read")
    string = string.replace("js_transfer", "main_init_transfer_javascript")
    string = string.replace("end()", "main_init_cleanup_super_variable()")
    
    new_string = string.split("\n")
    new = []
    expected = 0
    exit = 0
    
    for line in new_string:
        if line == new_string[-1]:
            if line ==("main_init_cleanup_super_variable()"):
                exit = 1
                break
            else:
                raise ValueError("Syntax error: Script not closed properly, cleanup not finished")

        if line.startswith("function"):
            line = line.replace("function", "def")

        if line.startswith("#include"):

            with open("config.ini","r") as f:
                data=f.read()

            # Get the path to the site packages folder

            path = data.split("site_packages_point=")[1].split("\n")[0]

            # Get each folder in the path location

            folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]

            if line.replace("#include ","") in folders:
                replaced=line.replace("#include ","")
                path_module=f"{path}/{replaced}.py"
                with open(path_module, "r") as f:
                    module=f.read()
                    # Import the module
                    exec(module)

            else:
                raise SyntaxError(f"Module {line.replace('#include ','')} not found")        
        if line.endswith("{"):
            line = line[:-1] + ":"
            expected += 1
        
        if line.endswith("}"):
            expected -= 1
            line = line[:-1]

        new.append(line)

    if expected != 0:
        print("Syntax error: Function not closed")
        return

    
    with open("logs/log.txt", "w+") as f:
        code = f.write("\n".join(new))

    exec("\n".join(new))    
    
    if exit == 1:
        main_init_cleanup_super_variable()



def compile_bee_file(input_file):
    with open(input_file, "r") as f:
        string = f.read()
        compiler(string)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: compiler.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    # Check if the file has the ".bee" extension
    if not input_file.lower().endswith(".bee"):
        print("Error: Invalid file extension. Please use a .bee file.")
        sys.exit(1)

    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"Error: File {input_file} not found.")
        sys.exit(1)

    # Call the function to compile the .bee file
    compile_bee_file(input_file)        