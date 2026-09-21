from random import randint, random

from src.HelperFunctions.merge import merge


def merge_sort(numbers:list[int],left:int,right:int)->list[int]:
    """
    Sorts and returns the given list of integers using mergesort.
    """
    if left < right:
        mid = (left+right) // 2
        merge_sort(numbers,left,mid)
        merge_sort(numbers,mid+1,right)
        merge(numbers,left,mid,right)
    return numbers
if __name__ == "__main__":
    repetitions = int(input("How many lists should be sorted?"))
    length = int(input("How many elements should each list contain?"))
    arr = [0] * length

    for i in range(repetitions):
        for j in range(length):
            arr[j] = randint(-10000000000,10000000000)
        merge_sort(arr,0,len(arr)-1)
        print(arr)
