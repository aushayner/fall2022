#include <stdio.h>
#include <limits.h>
#include <float.h>

int main(){

    //define variables
    char c;
    unsigned char uc;
    short s;
    int i;
    unsigned int ui;
    unsigned long ul;
    float f;

    //print statement for char
    printf("The size of a char is %d bytes.\n", sizeof(c));
    printf("The minimum value of an char is %d.\n", CHAR_MIN);
    printf("The maximum value of an char is %d.\n\n", CHAR_MAX);
    //print statements for unsigned char
    printf("The size of an unsigned char is %d bytes.\n", sizeof(uc));
    printf("The minimum value of an unsigned char is %d.\n", 0);
    printf("The maximum value of an unsigned char is %d.\n\n", UCHAR_MAX);
    //print statements for short
    printf("The size of a short is %d bytes.\n", sizeof(s));
    printf("The minimum value of a short is %d.\n", SHRT_MIN);
    printf("The maximum value of a short is %d.\n\n", SHRT_MAX);
    //print statements for int
    printf("The size of an int is %d bytes.\n", sizeof(i));
    printf("The minimum value of an int is %d.\n", INT_MIN);
    printf("The maximum value of an int is %d.\n\n", INT_MAX);
    //print statments for unsigned int
    printf("The size of an unsigned int is %d bytes.\n", sizeof(ui));
    printf("The minimum value of an unsigned int is %d.\n", 0);
    printf("The maximum value of an unsigned int is %d.\n\n", UINT_MAX);
    //print statments for unsigned long
    printf("The size of an unsigned long is %d bytes.\n", sizeof(ul));
    printf("The minimum value of an unsigned long is %lu.\n", 0);
    printf("The maximum value of an unsigned long is %lu.\n\n", ULONG_MAX);
    //print statements for float
    printf("The size of a float is %d bytes.\n", sizeof(f));
    printf("The minimum value of a float is %ld.\n", 0);
    printf("The maximum value of a float is %ld.\n\n", FLT_MAX);


}