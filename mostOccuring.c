#include<stdio.h>
#include<limits.h>

int getMaxCountElement(int *array, int size, int K) {
    int i, max, maxElementIndex;

    for(i = 0; i < size; i++) {
        array[array[i]%K] += K;	
    }
 
    max = array[0]; maxElementIndex = 0;
    for (i = 1; i < size; i++) {
        if (array[i]/K > max) {
            max = array[i]/K;
            maxElementIndex = i;
        }
    }

   return maxElementIndex;
}
int main()
{
    int arr[10];
    int array_size = 0, i = 0;
    scanf("%d",&array_size);
    for(i;i<array_size;i++){
        scanf("%d",&arr[i]);
    }
    printf("%d\n", getMaxCountElement(arr, array_size, array_size));
     
    return 0;
}