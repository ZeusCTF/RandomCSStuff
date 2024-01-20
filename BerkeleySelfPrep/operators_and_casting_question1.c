//Q1: Explain the difference between these two functions

#include <stdio.h>

int main() {
    int x, y, z;
    x = y = z = 1;
    x += (y += z);
    printf("%d %d %d\n", x, y, z);
}
/*
In this program, the output should be: 3, 2, 1
*/
 
 int main2() {
    int x, y, z;
    x = y = z = 1;
    (x += y) += z;
    printf("%d %d %d\n", x, y, z);
}
/*
I get an error in VS Code indicating that main2 will cause compilation to fail due to syntax issues.  
Attempting to compile with gcc does indeed fail.

My assumption for what this code would theoretically produce is something like: 2, 1, 3
However I could also understand a result of 2, 1, 2, assuming that the compiler is unable to correctly determine what to increment first
*/