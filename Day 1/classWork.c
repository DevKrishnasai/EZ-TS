#include<stdio.h>
#include<stdlib.h>
struct ex{
    int a;
    short b;
    char c;
}s;
void main(){
    //with padding = to align the datatypes
    //based on the highest data type the cyclic bits is set and size of struct is found
    // here higest data type is int so cyclic bits is 4 bytes
    // int a =====    4 * 1 = 4   4%4 === 0
    // short b =====  2 * 1 = 2   4%2 === 0
    // char c ======  1 * 1 = 1   4%1 === 0
    //the complier will add padding to align the datatypes so it adds 1 to this to become 8 from 7
    //the size will be in even numbers only
    printf("Size of structure: %d",sizeof(s)); //7+1 = 8
}

