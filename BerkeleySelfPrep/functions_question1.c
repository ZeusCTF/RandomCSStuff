//Q1: What is the output of the following program?
#include <stdio.h>

#define SIZE 3

int sum(int a1[], int a2[]) {
    int sum = 0;

    for (int i = 0; i < SIZE; i++) {
        a1[i] += a2[i];
        sum += a1[i];
    }
    return sum;
}

int main() {
    int array1[SIZE] = {1,2,3};
    int array2[SIZE] = {1,2,3};

    int x = sum(array1, array2);

    for (int i = 0; i < SIZE; i++) {
        printf("%d + %d", array1[i], array2[i]);
        if (i < SIZE - 1) printf(" + ");
    }
    printf(" = %d\n", x);
}