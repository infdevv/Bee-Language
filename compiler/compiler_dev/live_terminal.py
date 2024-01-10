# Basic command-line terminal 

from time import sleep

last_print=""

while True:
    with open("live_trm/live_terminal.txt", "r") as f:
        content = f.read()

    if (content == "-+clear+-"):
        amt=150
        while (amt > 0):
            amt=amt-1
            print(" ")
            last_print=""       
    elif (content == "-+end_stream+-"):
        break         
    else:
        if (content == last_print):
            x=1
        else:
            print(content)
            last_print=content
    sleep(1)           

