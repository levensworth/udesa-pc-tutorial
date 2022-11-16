#include <stdlib.h>
#include <stdio.h>
#include <math.h>

float calculateNearestPoint(float current[], float pointA[], float pointB[], float nearest[]);
float getDistanceBetweenPoints(float pointA[], float pointB[]);

int main(void)
{
    
    float currentPosition[2] = {0, 0};
    float p1[2] = {0, 658};
    float p2[2] = {576, 0};
    
    float nearest[2] = {0};

    float distance = calculateNearestPoint(currentPosition, p1, p2, nearest);
    printf("The nearest point is at (%f, %f) which is at %f mts.", nearest[0], nearest[1], distance);
    
    return 0;
}

float calculateNearestPoint(float current[], float pointA[], float pointB[], float nearest[])
{
    // given a current location and 2 points returns the nearest point
    float distanceToA = getDistanceBetweenPoints(current, pointA);
    float distanceToB = getDistanceBetweenPoints(current, pointB);
    
    if(distanceToA < distanceToB)
    {
        nearest[0] = pointA[0];
        nearest[1] = pointA[1];
        return distanceToA;
    }
    
    nearest[0] = pointB[0];
    nearest[1] = pointB[1];
    return distanceToB;
    
}


float getDistanceBetweenPoints(float pointA[], float pointB[])
{
    float distance;
    distance = pow(pointA[0] - pointB[0], 2) + pow(pointA[1] - pointB[1], 2);
    return sqrt(distance);
}
