from plusz import iras_time
from plusz import speed
from plusz import diaOff
import time




def mergeSort(array):
    if len(array) >=20 or diaOff:
        iras_time(f'Merge...') 
    else:
        iras_time(array, dia=True, time_interval=0.1) 

    al = len(array)
    if al == 1:
        return array
    
    array_L = mergeSort(array[0:al//2])
    
    array_R = mergeSort(array[al//2:al])
    for _ in range(al):
        time.sleep(speed)
        if len(array) >=20 or diaOff:
            iras_time(f'Merge...') 
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
    return array