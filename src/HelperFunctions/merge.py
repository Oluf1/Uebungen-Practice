def merge(array:list[int],left:int,mid:int,right:int):
    """
    Sorts a subsection of an array by splitting it into two and then merging it again, both subsections have to be sorted.
    """
    indices_left = mid - left +1
    indices_right = right -mid
    L = [0]*indices_left
    R = [0]*indices_right

    for i in range(indices_left):
        L[i] = array[left+i]
    for j in range(indices_right):
        R[j] = array[mid+1+j]
    i = 0
    j = 0
    k = left
    # the While loop merges the subarrays into a single sorted one, both subarrays need to be sorted for the resulting array to be sorted.
    while i < indices_left and j < indices_right:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k +=1
    while i < indices_left:
        array[k] = L[i]
        i += 1
        k+=1
    while j < indices_right:
        array[k] = R[j]
        j+=1
        k+=1
