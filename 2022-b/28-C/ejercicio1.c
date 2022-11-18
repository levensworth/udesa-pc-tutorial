#include <stdio.h>
#include <stdlib.h>


void copy_array(int * arr_out, int * arr_in, int n);
void print_array(int * arr, int size);

int main(void)
{
    int v[] = {2, 4, 6, 8, 10, 12, 14, 16} ;
    int v2[10];

    copy_array(v2, v, 8);
    
    print_array(v, 8);
    return 0;
}


void copy_array(int * arr_out, int * arr_in, int n)
{
    for(int i =0; i < n; i++)
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

    printf(" %d]\n", arr[size-1]);
}