#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define DIMENSION 4

float innerProduct(float vecA[], float vecB[])
{
    float result = 0;

    for(int i=0; i < DIMENSION; i++){
        result += vecA[i] * vecB[i];
    }
    
    return result;
}


float getVectorNorm(float vec[])
{
    return sqrt(innerProduct(vec, vec));    
}

void normalizeVector(float vec[])
{
    float norm = getVectorNorm(vec);

    for(int i = 0; i < DIMENSION; i++)
    {
        vec[i] /= norm;    
    }

}

void toString(float vec[])
{
    printf("[");
    for(int i=0; i < DIMENSION ; i++)
    {   
        printf("%.2f ", vec[i]);
    }
    
    printf("]\n");
}


int main(void)
{
    float vec[DIMENSION] = {1, 2, 3, 4};    
    float norm = getVectorNorm(vec);

    printf("el vector:");
    toString(vec);
    printf("tiene de norma %f\n", norm);

    printf("el vector normalizado es:");
    normalizeVector(vec);
    toString(vec);

}
