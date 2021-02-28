import time


def partition_quick(array, start, end):
   pivot = array[start]
   low = start + 1
   high = end

   while True:
       while low <= high and array[high]>= pivot:
           high = high -1
           
       while low <= high and array[low] <= pivot:
            low = low +1
       if low <= high:
            array[low], array[high] = array[high], array[low]
       else:
            break
        
   array[start], array[high] = array[high], array[start]

   return high

def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition_quick(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)
    
    
def bubble_sort(data, drawData, timeTick):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data)
                time.sleep(timeTick)
    drawData(data)