#include <stdio.h>

union MyUnion {
    int a;
    double b;
    short c;
    char d[1000];
}s;

void main()
{
    // based on the highest data type size the union depends
    //here char had 1000 size so size of union is 1000
    printf("Size of union: %d", sizeof(s));
}
