#include "merge.h"
#include <stdlib.h>
#include <time.h>
#include "stdio.h"

void mergesort(int array[],int left,int right){
    int mid;
    if (left<right){
        mid = (left+right) / 2;
        mergesort(array,left,mid);
        mergesort(array,mid+1,right);
        merge(array,left,mid,right);
    }
}


int main(){
    srand((unsigned)time(NULL));
    int indices = 100;
    int array[indices];
    for (int i=0;i<indices;i++){
        array[i] = rand() % 101;
    }
    mergesort(array,0, indices);
    for (int i = 0;i<indices;i++){
        printf("%d ,",array[i]);
    }
}
