//Q2: What does the following code print?
#include <stdio.h>

int main() {
    struct {
    char s[3];
    int i;
    } x;
/*
Defines a structure x, that has a character array and integer value
*/

    printf("%d\n", (char *)&x.i - x.s); // the cast here converts the address of x.i to a char pointer, then subtracts this from x.s.  This should be 4
    printf("%d\n", sizeof(x) - sizeof(x.s) - sizeof(x.i)); // This subtracts the size of the structure, the char array, and the integer.  This should be 1
}
