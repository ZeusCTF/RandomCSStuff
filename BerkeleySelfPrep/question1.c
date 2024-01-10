//Q1: What numbers are printed by the following loops?
#include <stdio.h>

int main() {
    for (int i = 0; i < 5; ++i)
        printf("loop 1: counter %d\n", i);
        //prints numbers: 0,1,2,3,4

    for (int i = 1; i <= 5; ++i)
        printf("loop 2: counter %d\n", i);
        //prints numbers: 1,2,3,4,5

    for (int i = 5; i > 0; --i)
        printf("loop 3: counter %d\n", i);
        //prints numbers: 5,4,3,2,1

    for (int i = 5; --i;)
        printf("loop 4: counter %d\n", i);
        //prints numbers: 4,3,2,1
    return 0;
}

