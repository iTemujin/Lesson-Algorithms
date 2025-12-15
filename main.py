import random
import os
import time


from plusz import iras
from plusz import backTime
from plusz import timer
from plusz import sorhagyas
from plusz import cls

from mergeSort import MergeSort
from bubbleSort import BubbleSort
from diagram import Dia

# Config

sortores_deafult = 3
default = 10
varkozasi_ido = 2
time_interval_default_for_text = 2
mode_has = {'all':'default', 'bubble':BubbleSort, 'merge':MergeSort}


this = []
def main():
    while True:
        szam, mode = better_input()
        iras("Mindem jo?")
        print(f"Szam: {szam}\nMode: {mode}")
        while True:
            x = input("Y/N: ")
            if x.lower() == 'y' or x.lower() == 'n':
                break
            iras("Kerlek csak y vagy n betut irj be!")
        if x.lower() == 'y':
            break


    iras("Remek!\nAkkor készítem a számokat...")
    
    backTime()

    make_mixer_numbers(szam)
    print(this)

    if 'all' in mode:
        mode = []
        for key, value in mode_has.items():
            if 'all' != key:
                mode.append(key)

    for _ in mode:
        iras(f"Elkezdeni a {_}-sort rendezést...")
        backTime()
        
        G = mode_has[_](this.copy())
        G.start()
        timer(True)
        timerr = timer()
        sorhagyas()
        print(f'{_.upper()} [DONE]')
        print(timerr)
        sorhagyas()


        ez = Dia()
        ez.run(G)

        




def better_input():
    while True:
        mode = ['all']  # default mode is 'all'
        try:
            val = input(f"Enter an integer (default {default}): ")
            if val == '':
                return default, mode
    
            val = val.split(' ')

            if val[0] in ['?', 'help', '-h', '--help']:
                iras(f"Input format: <number> ['*' or 'x' <multiplier>] [^|** <exponent>] [--mode <modes>]\nExamples:\n  100\n  10 * 3 \n  20 ** 10 \n 4000 * 50 bubi \n 3000 * 40 {mode_has[1]} temualgi etc... \n 6000 --mode bubi etc... \nModes:\n  {mode_has[0]} - run all algorithms (default)\n  {mode_has[1]} - run {mode_has[1]} sort\n")
                continue

            try:
                szam = int(val[0])
            except:
                iras("First argument must be a number. [write ? for help]")
                continue


            if len(val) >= 3:
                if val[1] == "*" or val[1] == "x":
                    szam = szam * int(val[2])
                elif val[1] == "^" or val[1] == "**":
                    szam = szam ** int(val[2])
            
                elif val[1] == "--mode":
                    mode = []
                    for m in val[2:]:
                        if m not in mode_has:
                            print(f"Dont have this mode: {m}")
                            continue
                    mode = val[2:]

            if len(val) >= 4 and val[1] != "--mode":
                for m in val[3:]:
                    if m not in mode_has:
                        print(f"Dont have this mode: {m}")
                        continue
                mode = val[3:]

            
            return szam, mode
        except ValueError:
            iras("Jujj! Nem tudom mi baja :D Próbáld újra mashogy!")



def make_mixer_numbers(input):
    for _ in range(input):
        this.append(_)
    random.shuffle(this)



if __name__ == "__main__":
    cls()
    main()


