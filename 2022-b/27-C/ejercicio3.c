#include <stdlib.h>
#include <stdio.h>

char toLower(char value)
{
    if(value < 'A' && value > 'Z')
        return value;

    return value + ('a' - 'A');
}

void toLowerString(char string[])
{
    int i = 0;
    while(string[i] != 0) {
        string[i] = toLower(string[i]);
        i++;
    }
}


int main(void)
{
    char string[5] = "HOLA";
    
    toLowerString(string);
    
    printf("%s\n", string);
    return 0;
}
