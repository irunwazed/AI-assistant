
import keyboard

from utils.translate import *
from utils.audio import *
from utils.websocket import *
from utils.tts import *
from utils.subtitle import *


import timeit

if __name__ == "__main__":
    start()

    print("Press and Hold Right Shift to record audio")
    while True:
        if keyboard.is_pressed('RIGHT_SHIFT'):
            try:

                # speech and convert to text
                # message = speech_to_text()
                message = input("Masukkan :")
                generate_subtitle("input.txt", message)

                # # send message to AI
                respon = send_message(message)


                # # translate answer to english
                generate_subtitle("output.txt", respon)
                # respon = translate_to_en(respon)

                
                detect = detect_google(message)
                # if detect == 'ID':
                #     respon = translate_to_id(respon)
                # say answer
                # pyttsx3_tts(respon)
                # google_tts(respon)
                edgetts_tts(respon, detect)


                # Clear the text files after the assistant has finished speaking
                time.sleep(1)
                with open ("output.txt", "w") as f:
                    f.truncate(0)
                with open ("input.txt", "w") as f:
                    f.truncate(0)

                
                # print(Fore.RED + "Press and Hold Right Shift to record audio")
                # print(Style.RESET_ALL)
            except:
                print("server error")

    close()
        