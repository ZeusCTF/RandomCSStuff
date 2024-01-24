// Q3: What do the following functions do?
#include <stdio.h>

void countu(unsigned n) {
    while (n-- >= 0)
    printf("%u\n count u", n);
}

void counti(int n) {
    while (n-- >= 0)
    printf("%d\n", n);
}

/*
Both functions perform the same general action, that being to decrement the n variable and print it to the screen as long as it is ge 0.
The difference between the two is that counti prints the resulting value as an integer while countu prints the value as an unsigned int.
But as an unsigned integer cannot be negative, this value will be represented as a very large positive integer > thus will continue to infinity.
*/
