#include <stdlib.h>
#include <stdio.h>

#define MAX_VAL 500
#define MIN_VAL -500

// headers
int generateRandomNumber(int minValue, int maxValue);


int main(void) 
{
    srand(42);
    int x = generateRandomNumber(MIN_VAL, MAX_VAL);
    int y = generateRandomNumber(MIN_VAL, MAX_VAL);

    float result;

    int op = 0;
    
    if (op == 0)
    {
        // suma
        result =  x + y;
        printf("Entradas: x=%d y=%d. Resultado x%sy = %f\n", x, y, "+",result);
    }

    if (op == 1)
    {
        // resta
        result = x - y;
        printf("Entradas: x=%d y=%d. Resultado x%sy = %f\n", x, y, "-", result);
    }
    
    if (op == 2)
    {
        // mult
        result = x * y;
        printf("Entradas: x=%d y=%d. Resultado x%sy = %f\n", x, y, "*", result);
    }

    if (op == 3)
    {
        // div
        result = x / y;
        printf("Entradas: x=%d y=%d. Resultado x%sy = %f\n", x, y, "/", result);
    }
    
    return 0;
}


int generateRandomNumber(int minValue, int maxValue)
{
    int dif = maxValue - minValue;

    return (int)(minValue + dif * rand());
}