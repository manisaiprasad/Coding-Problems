void segregate0and1(int array[], int size)
{
    int left = 0, right = size-1;
 
    while (left < right)
    {
        while (array[left] == 0 && left < right)
            left++;
        while (array[right] == 1 && left < right)
            right--;
        if (left < right)
        {
            array[left] = 0;
            array[right] = 1;
            left++;
            right--;
        }
    }
}
 
int main()
{
    int arr[10];
    int array_size = 0, i = 0;
    scanf("%d",&array_size)
    for(i,i<array_size,i++){
        scanf("%d",&arr[i])
    }
    segregate0and1(arr, array_size);
    for (i = 0; i < 6; i++)
        printf("%d ", arr[i]);
    getchar();
    return 0;
}