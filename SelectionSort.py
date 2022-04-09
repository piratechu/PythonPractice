from re import I
import sqlite3


def SelectionSort(sequence):
    index_length = range(0, len(sequence)-1)
    for i in index_length:
        min_value = i
        for j in range(i+1,len(sequence)):
            if sequence[j] < sequence[min_value]:
                min_value = j
        if min_value !=i :
            sequence[min_value], sequence[i] = sequence[i], sequence[min_value]
    
    return sequence
    

print(SelectionSort([7,3,5,3,27,4,9,4]))


