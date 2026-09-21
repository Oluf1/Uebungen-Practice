def merge(array:list[int],left:int,mid:int,right:int):
    """
    Merges two unsorted arrays into one Sorted array
    """
    indicies_left = mid - left +1
    indicies_right = right -mid
    L = [0]*indicies_left
    R = [0]*indicies_right

    for i in range(indicies_left):
        L[i] = array[left+i]
    for j in range(indicies_right):
        R[j] = array[mid+1+j]
    i = 0
    j = 0
    k = left
    # the While loop merges the subarrays into a single sorted one, both subarrays need to be sorted for the resulting array to be sorted.
    while i < indicies_left and j < indicies_right:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k +=1
    while i < indicies_left:
        array[k] = L[i]
        i += 1
        k+=1
    while j < indicies_right:
        array[k] = R[j]
        j+=1
        k+=1
