//Q1: What is the output of the following code?
#include <stdio.h>

int main(){
    int ary[4] = {11, 22, 33, 44};
    int *ptr;

    ptr = ary;

    for (int i = 0; i < 4; i++)
    {
        printf("%d %p\n", *ptr, ptr);
        ptr++;
    }//prints the integers in ary, along with their locations in memory

}