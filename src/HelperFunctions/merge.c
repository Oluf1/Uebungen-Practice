#include "merge.h"

void merge(int array[], int left, int mid, int right){
    // counter declarations
    int j;
    int i;
    int k = left;
    //
    int indices_left = mid-left+1;
    int indices_right = right-mid;
    // declare arrays
    int L[indices_left];
    int R[indices_right];

    for (i = 0; i < indices_left; i++) {
        L[i] = array[left+i];
    }
    for (j = 0; j<indices_right; j++) {
        R[j] = array[mid+j+1];
    }

    i = 0;
    j = 0;
    while (i < indices_left && j < indices_right){
        if(L[i] <= R[j]) {
            array[k] = L[i];
            i++;
        }
        else  {
            array[k] = R[j];
            j++;
        }
        k++;
    }
    while (i < indices_left){
        array[k] = L[i];
        k++;
        i++;
    }

    while (j<indices_right) {
        array[k] = R[j];
        k++;
        j++;
    }
}
