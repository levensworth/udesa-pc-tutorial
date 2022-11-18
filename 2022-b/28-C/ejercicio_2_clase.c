#include <stdio.h>
#include <stdlib.h>

#define INCHES_TO_CENIMETERS 2.54

int showMenuAndSelect(void);
float computeCentimeterToInches(void);
float computeInchesToCentimeter(void);

int main(void)
{
    int option = showMenuAndSelect();
    float result;

    if(option == 1)
    {
       result = computeCentimeterToInches();
       printf("El resultado es %.2f\n", result);
    }
    else if(option == 2)
    {
        result = computeInchesToCentimeter();
        printf("El resultado es %.2f\n", result);
    }
    else if(option == 3)
    {
        printf("Bye!\n");
    }
    else
    {
        printf("Le pifiaste\n");
    }

    return 0;
}


int showMenuAndSelect(void)
{
    int option;
    printf("[1] Convertir cm a pulgadas\n");
    printf("[2] Convertir pulgadas a cm\n");
    printf("[3] Salir\n");
    
    scanf("%d", &option);
    return option;
}

float computeCentimeterToInches(void)
{   
    float centimeters;
    printf("Que valor deseas convertir: \n");
    scanf("%f", &centimeters);
    
    float inches = centimeters / INCHES_TO_CENIMETERS;
    
    return inches;
}

float computeInchesToCentimeter(void)
{
    float inches;
    printf("Que valor deseas convertir: \n");
    scanf("%f", &inches);
    
    float centimeters = inches * INCHES_TO_CENIMETERS;
    
    return centimeters;
}