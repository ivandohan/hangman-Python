# Created by : Ivandohan Samuel Siregar

# Project ini masih jauh dari kata "sempurna"
# Jika kalian punya ide dan masukan, silahkan beri pull request pada repository github project

# Project ini saya buat dengan versi Bahasa Indonesia

'''
    Soon = [
        "Project menggunakan Bahasa Inggris",
        "The project will be in English",
        "Refactoring project in to Go Language"
    ]
'''

import random

from os import system
from interface import logo, stages
from data import word_list, chance

end_of_game = False
display = []
chosen_word = random.choice(word_list)
_chance = chance
message = ""

for _ in range(len(chosen_word)):
    display.append("_")

while not end_of_game:
    print(logo)
    print("\n")

    # Ditampilkan saat proses pengembangan project
    # Atur baris 37 sebagai "comment line" jika ingin bermain
    print(f"Psssttt, jawabannya {chosen_word}")

    print(f'''    
        Tebakan kamu : {" ".join(display)}
    ''')

    user_input = input("Tebak sebuah huruf : ")

    system('cls')

    if user_input in display:
        message = "Kamu sudah menginput huruf ini!"

    for i in range(len(chosen_word)):
        if chosen_word[i] == user_input:
            display[i] = user_input

    if user_input not in chosen_word:
        message = f"Huruf {user_input} tidak tersedia! Nyawamu berkurang -1."
        _chance -= 1
        if _chance == 0:
            end_of_game = True
            print("Kamu Kalah. Tidak ada kesempatan lagi.")

    if "_" not in display:
        end_of_game = True
        print("Yeayy, kamu berhasil menebaknya!")

    print(stages[_chance])
    if _chance != 0 and not end_of_game:
        print(message)




