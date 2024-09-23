#include <stdio.h>

//fun_struct definition
struct fun_struct{
    int x;
    int y; 
    int z;
} fun_struct;

//function prototypes
int structCompare(struct fun_struct a, struct fun_struct b);



int main()
{
    //initialize structures
    struct fun_struct a;
    struct fun_struct b;

    //Initialize member variables
    a.x = 0;
    a.y = 1;
    a.z = 3;

    b.x = 4;
    b.y = 2;
    b.z = 1;

    //compare the structures and print the results
    int trueFalse = structCompare(a, b);

    if(trueFalse == 1){
        printf("The two variables are equal\n\n");
    }else{
        printf("The two variables are not equal\n\n");
    }

    //re-assign the b variables to be equal to a
    b.x = a.x;
    b.y = a.y;
    b.z = a.z;

    //Compare the two sturctures again
    //compare the structures and print the results
    trueFalse = structCompare(a, b);

    if(trueFalse == 1){
        printf("The two variables are equal\n\n");
    }else{
        printf("The two variables are not equal\n\n");
    }

}

int structCompare(struct fun_struct a, struct fun_struct b){

    if(a.x != b.x){
        return 0;
    }
    else if(a.y != b.y){
        return 0;
    }
    else if(a.z != b.z){
        return 0;
    }

    return 1;

}