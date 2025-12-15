import os
import time

sortores_deafult = 3
default = 10
varkozasi_ido = 2
time_interval_default_for_text = 1.3
diaOff = True
speed = 0


was = 0
def timer(start=False):
    global was
    if start:
        was = time.time()
        return  
    return f'{round(time.time() - was, 3)}sec'


def sorhagyas(input=sortores_deafult):
    s = ''
    for _ in range(input):
        s = s+'\n'
    print(s)


def cls():
    os.system('cls')

time_was = 0
def iras_time(text, time_interval=time_interval_default_for_text, dia=False):
    global time_was
    time_now = time.time() 
    if time_was <= time_now:
        cls()
        if dia:
            for _ in text:
                for i in range(_):
                    print('#', end='', flush=True)
                print()
        else:
            print(text)

        time_was = time_now + time_interval
        return time_now + time_interval
    return time_was

def backTime(vissza=varkozasi_ido):
    print(f"{vissza}.. --> ..1")
    for _ in range(vissza):
        print(f"{vissza-_}", end="", flush=True)
        for i in range(3):
            print(".", end="", flush=True)
            time.sleep(0.33)


def iras(x):
    cls()
    print(x)
