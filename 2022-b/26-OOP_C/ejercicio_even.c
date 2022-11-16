# include <stdio.h>
# include <stdbool.h>

bool isEven(int x);
void printEvens(int max);

int main(void)
{
    printEvens(100);
    return 0;
}


void printEvens(int max)
{
    for(int i = 0; i < max; i++)
    {
        if(isEven(i))
            printf("el num %d es par\n", i);
    }
}

bool isEven(int x)
{
    if(x % 2 == 0)
        return true;

    return false;
}



