from plusz import iras_time
from plusz import speed
from plusz import diaOff
import time
from threading import Thread


class MergeSort(Thread):
    def __init__(self, array):
        super().__init__()
        self.array = array
        self.now_array = []
        

    def run(self):
        print(self.mergeSort(self.array))
        return 0
    
    def get(self):
        return self.array

    def getThat(self):
        return self.now_array

    def mergeSort(self, array, index=0):
        self.now_array = array
        if len(array) >=4 or diaOff:
            iras_time(f'Merge... {index}') 
        else:
            iras_time(array, dia=True, time_interval=0.1) 

        al = len(array)
        if al == 1:
            return array
        
        array_L = self.mergeSort(array[0:al//2], index)
        
        array_R = self.mergeSort(array[al//2:al], index+al//2)
        for _ in range(al):
            self.now_array = array
            time.sleep(speed)
            if len(array) >=4 or diaOff:
                iras_time(f'Merge... {index}') 
            else:
                iras_time(array, dia=True, time_interval=0.1)


            if len(array_L) == 0:
                array[_] = array_R[0]
                del array_R[0]
                continue
            if len(array_R) == 0:
                array[_] = array_L[0]
                del array_L[0]
                continue

            if array_L[0] < array_R[0]:
                array[_] = array_L[0]
                del array_L[0]
            else:
                array[_] = array_R[0]
                del array_R[0]
            
            self.array[index+_] = array[_]

        return array