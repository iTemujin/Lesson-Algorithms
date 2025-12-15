from plusz import iras_time
from plusz import speed
import time

from threading import Thread

class BubbleSort(Thread):
    def __init__(self, array):
        super().__init__()
        self.array = array

    def run(self):
        print('szia bubbleSort')
        percent = len(self.array) // 100
        while True:
            time.sleep(speed)
            change = 0
            was = False
            for i in range(len(self.array)-1):
                if self.array[i] > self.array[i+1]:
                    if was is False:
                        was = True
                    
                    self.swap(i, i+1)
                    change += 1

            if len(self.array) <=20:
                iras_time(self.array, dia=True, time_interval=0.1)
            else:
                iras_time(f'Bubble... {100-change//percent}')

            if was is False:
                break

        return self.array
    

    def swap(self, a, b):
        if not (0 <= a < len(self.array)) or not (0 <= b < len(self.array)):
            raise IndexError("Index out of bounds")
        self.array[a], self.array[b] = self.array[b], self.array[a]

    def get(self):
        return self.array

