//Q1: What is the output of the following program?
#include <stdio.h>

#define SIZE 3

int sum(int a1[], int a2[]) {
    int sum = 0;

    for (int i = 0; i < SIZE; i++) {
        a1[i] += a2[i];
        sum += a1[i];
    }
    /*
    loop 1 -> a1[i] = 2, sum = 2
    loop 2 -> a1[i] = 4, sum = 6
    loop 3 -> a1[i] = 6, sum = 12
    */
    return sum;
}

int main() {
    int array1[SIZE] = {1,2,3};
    int array2[SIZE] = {1,2,3};

    int x = sum(array1, array2);
    //x contains 12

    // Printing the entire array using a for loop
    printf("Elements of the array: ");
    for (int j = 0; j < SIZE; ++j) {
        printf("%d ", array1[j]);
    }
    printf("\n");




    for (int i = 0; i < SIZE; i++) {
        printf("%d + %d", array1[i], array2[i]);
        /*
        loop 1 -> 2 + 1
        loop 2 -> 4 + 2
        loop 3 -> 6 + 3
        */
        if (i < SIZE - 1) printf(" + ");
        //checks of i is at the final value, if it is, then don't print a +
    }
    printf(" = %d\n", x);
    //prints the sum value calculated earlier
}