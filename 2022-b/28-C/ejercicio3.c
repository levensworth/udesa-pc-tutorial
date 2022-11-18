#include <stdio.h>

void swapcase(char * text, int len);
int isUpper(char a);
int isLower(char a);
char swap(char value);

int main(void)
{
    char string[] = "HolA Soy Santiago!!";
    
    printf("%s\n", string);
    swapcase(string, sizeof(string));
    printf("%s\n", string);

    return 0;    
}

void swapcase(char * text, int len)
{
    for(int i = 0; i < len; i++)
    {
        text[i] = swap(text[i]);
    }
}

char swap(char value)
{
    int delta = 'a' - 'A';
    
    if(isLower(value))
        return value - delta;
    if(isUpper(value))
        return value + delta;
    
    return value;
}

int isLower(char a)
{
    if(a >= 'a' && a <= 'z')
        return 1;
    
    return 0;
}

int isUpper(char a)
{
    if(a >= 'A' && a <= 'Z')
        return 1;
    
    return 0;
}

