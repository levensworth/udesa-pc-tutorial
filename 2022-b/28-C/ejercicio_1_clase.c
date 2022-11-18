#include <stdio.h>

void copy_array(int * arr_out, int * arr_in, int n);
void print_array(int * arr, int size);

int main(void)
{
    int original[] = {};
    int size = 0;
    int copy_vec[size];
    copy_array(copy_vec, original, size);
    
    print_array(original, size);
    print_array(copy_vec, size);

    return 0;
}

void copy_array(int * arr_out, int * arr_in, int n)
{
    for(int i = 0; i < n; i++)
    {
        arr_out[i] = arr_in[i];
    }
}

void print_array(int * arr, int size)
{
    printf("[");
    for(int i = 0; i < size-1; i++)
    {
        printf(" %d,", arr[i]);
    }
    
    if(size != 0)
    {
        printf(" %d", arr[size-1]);
    }

    printf("]\n");
}
