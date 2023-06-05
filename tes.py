

# from utils.audio import *
# from utils.translate import *

# from utils.tts import *

# text  = '''
# Iya, jadi London itu di Britinya, Britain itu di negara di benua eropa, Benua eropa itu satu benua di planet bumi, planet Bumi itu di tata surya, dan tata surya itu ada di galaksi milkway, 
# dan galaksi milkway itu ada di alam semesta, dan alam semesta ini 
# ada di dimensi, dimensi itu ada banyak, tapi semua itu ada di penciptanya alam semesta ini.
# Iya, jadi London itu di penciptanya alam semesta :)
# '''
# # silero_tts(text)

# import timeit
# # record_audio()

# text = '何？日本語を話して下さい'
# text = 'こんにちは。私はキルアです'

# start = timeit.default_timer()
# detect = detect_google(text)
# print(text)
# print(detect)
# edgetts_tts(text, detect)

# stop = timeit.default_timer()
# lama_eksekusi = stop - start
# print("edge_tts2 : "+str(lama_eksekusi))

import openai


openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)

prompt = [
    {"role": "user", "content": "Kamu adalah Kirua Kinagi. kamu dibuat oleh AKA. tujuan kamu dibuat untuk membantu manusia dalam belajar teknologi modern. kamu sangat senang dengan teknologi. "},
    {"role": "system", "content": f"Below is conversation history.\n"},
    {"role": "user", "content": f"AKA said halo bro.\n"},
]

response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=prompt,
        max_tokens=128,
        temperature=1,
        top_p=0.9
    )

# response = openai.Completion.create(
#   model="gpt-3.5-turbo",
#   prompt="Halo Siapa namamu?"
# )

print(response)
