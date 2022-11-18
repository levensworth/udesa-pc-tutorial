#include <stdio.h>
#include <stdlib.h>

#define INCHE_IN_CM 2.54

int showMenuAndSelect(void);
float centimeterToInches(void);
float inchesToCentimeters(void);


int main(void)
{
    int selection = showMenuAndSelect();
    
    if(selection == 1)
    {
        float result = centimeterToInches();
        printf("result: %.2f inches\n", result);
    } 
    else if(selection == 2)
    {
        float result = inchesToCentimeters();
        printf("result: %.2f inches\n", result);
    } 
    else if(selection == 3)
    {
        printf("Bye\n");
    }
    else{
        printf("Error, unknown selection.");
        return 1;
    }

        
    
    return 0;
}


int showMenuAndSelect(void)
{
    printf("Las opciones:\n[1] Convertir cm a pulgadas\n[2] Convertir pulgadas a cm\n[3] Salir\n");
    int selection;
    scanf("%d", &selection);
    return selection;
}

float centimeterToInches(void)
{
    float centimeters;
    printf("input the amount in centimeters: ");
    scanf("%f", &centimeters);
    return centimeters / INCHE_IN_CM;   
}

float inchesToCentimeters(void)
{
    float inches;
    printf("input the amount in inches: ");
    scanf("%f", &inches);
    
    return inches * INCHE_IN_CM;
}
