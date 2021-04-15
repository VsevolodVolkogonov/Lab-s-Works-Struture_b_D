import random
import numpy as np
ch_array = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
random.shuffle(ch_array)
def check(ch_array):
    generator_done = 0
    if generator_done ==0 :
        print(ch_array)
        zero_row = 0
        zr = ch_array.index(0)
        if zr <=3:zero_row=1
        if 3< zr <=7:zero_row=2
        if 7<zr<=11 :zero_row=3
        if 11 < zr <= 15:zero_row=4
        print(zr + 1 ,zero_row)

        this_sum = 0

        for i in range(len(ch_array)-1):
            val1=ch_array[i]
            if val1 !=0:
                j = i+1
                for j in range(len(ch_array)):
                    val2=ch_array[j]
                    if val1 > val2 and val2!=0: this_sum+=1

        this_sum +=zero_row
        if this_sum % 2 == 0:
            print("нерешаемо ")
            random.shuffle(ch_array)
        else:
            print("возможно решить - исходные данные : ")
            print(ch_array)
check(ch_array)


