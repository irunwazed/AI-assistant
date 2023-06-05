from websocket import create_connection
from colorama import *

ws = None

def start():
    global ws
    ws = create_connection("ws://localhost:40102/")

def close():
    global ws
    ws.close()

def send_message(message):
    global ws
    try:
        # print(Fore.GREEN + Style.BRIGHT + message  + Fore.RESET , end="", flush=False)
        print(Fore.GREEN + message)
        print(Style.RESET_ALL)

        ws.send(message)
        result = ws.recv()

        print("System : "+Fore.YELLOW + result)
        print(Style.RESET_ALL)
        
        # print("\rSystem " + Fore.YELLOW + Style.BRIGHT +  ": " + result  + Fore.RESET , end="", flush=False)

        return result
    except:
        return "Saya adalah karakter baru. Maaf saya tidak mengerti yang anda katakan. Bisa ulangi?"
