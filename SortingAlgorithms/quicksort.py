import time

def swap(lyst, i, j):
 
 temp = lyst[i]
 lyst[i] = lyst[j]
 lyst[j] = temp

def quicksort(lyst):
    quicksortHelper(lyst, 0, len(lyst) - 1)

def quicksortHelper(lyst, left, right):
    if left < right:
        pivotLocation = partition(lyst, left, right)
        quicksortHelper(lyst, left, pivotLocation - 1)
        quicksortHelper(lyst, pivotLocation + 1, right)

def partition(lyst, left, right):
    
    middle = (left + right) // 2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot

    
    boundary = left

    
    for index in range(left, right):
        if lyst[index] < pivot:
            swap(lyst, index, boundary)
            boundary += 1

    
    swap(lyst, right, boundary)
    return boundary


import random
tamanho=[1000,10000,100000,1000000]
def main(size, sort = quicksort):
 lyst = []
 for count in range(size):
    lyst.append(random.randint(1, size + 1))
 start=time.time()
 sort(lyst)
 print(time.time()-start)
 

for item in tamanho:
   main(item)
input()

   
