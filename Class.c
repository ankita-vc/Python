#include<stdio.h>
#include<stdlib.h>

struct Demo
{
    int X;
    int Y;
    char ch;
    float F;

    
};

int main()
{
    struct Demo obj;
    struct Demo obj2;

    obj.X= 11;
    printf("%d", obj.X);

    return 0;
}