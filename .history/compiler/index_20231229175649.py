import sys
import os
import subprocess
import asyncio
import random
from pathlib import Path

version=1.2



"""

Bee# Compiler

bee# will be the first language to be a super set of a lanngugage yet stil be able to run another language

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

def main_init_transfer_javascript(code):
    random_name = str(random.randint(100000, 999999))
    js_file_path = Path(f"temp/{random_name}.js")

    with js_file_path.open("w") as f:
        f.write(code)

    try:
        subprocess.run(["node", "--version"], check=True)
    except subprocess.CalledProcessError:
        raise SyntaxError("Error: Node.js is not installed or not available. Please install Node.js and try again.")

    js_runner_path = Path("js_runner.js")
    
    with js_runner_path.open("w+") as f:
        f.write(code)

    subprocess.Popen(["node", str(js_runner_path)])

    print("Swapped to javascript")
    quit()

# Other functions remain unchanged...

def main_init_javascript_runner(code, runtime):
    if not runtime:
        print("No runtime specified. Automatically setting runtime to 1000ms")
        runtime = 1000

    try:
        subprocess.run(["node", "--version"], check=True)
    except subprocess.CalledProcessError:
        raise SyntaxError("Error: Node.js is not installed or not available. Please install Node.js and try again.")

    random_name = str(random.randint(100000, 999999))
    js_file_path = Path(f"temp/{random_name}.js")

    with js_file_path.open("w") as f:
        f.write(code)

    try:
        subprocess.run(["node", str(js_file_path)], timeout=runtime / 1000)
    except subprocess.TimeoutExpired:
        if sys.platform == "win32":
            subprocess.run(["taskkill", "/f", "/im", "node.exe"])
        else:
            subprocess.run(["pkill", "node"])
    finally:
        os.remove(js_file_path)

def main_init_cleanup_super_variable():
    print("")   

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
    exit = 1
    
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
           
           command = ["com.bat", (line.replace("#include ", ""))]
           # Use subprocess to run the command
           try:
             subprocess.run(command, check=True)
           except subprocess.CalledProcessError as e:
                print(f"Error while importing module: {e}")

            # Get the new content

            with open(line.replace("#include ", ""), "r") as f:
                exec(f.read())

            # Now brutally fuck the file up, aka delete it

            os.remove(line.replace("#include ", ""))          

         except FileNotFoundError:
            raise FileNotFoundError(f"Module {line.replace('#include ', '')} was not found.")
         except Exception as e:
             raise SyntaxError(f"Error executing module {line.replace('#include ', '')}: {str(e)}")
   
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

    
    
    #print("\n".join(new))
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