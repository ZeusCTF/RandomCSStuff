// Q2: What output does the following code produce?
#include <stdio.h>

int main() {
    int array[3];
    int i = 3, x = 3;

    while (--i && (array[i] = --x))
          printf("%d\n", array[i]);
};

/*
This code will output:
2
1

This will happen because x will reach 0 before the last element is added to the array, breaking out of the loop
*/