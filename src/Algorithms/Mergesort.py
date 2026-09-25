from random import randint

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
    length = int(input("How many elements should each list contain?"))
    arr = [0] * length
    for j in range(length):
        arr[j] = randint(0,1000000)
    merge_sort(arr,0,len(arr)-1)
    print(arr)
