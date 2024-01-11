//Q2: What output does the following code produce?
#include <stdio.h>

int main() {
int x, y;
int i = 3;
x = y = 0;

while (i >= 0) {
    x += 1;
    i--;
} //sets x = 3, i = 0
do {
    y += 1;
    i++;
} while (i <= 3); //ends with y = 4, i = 4
printf("%d\n", (x-y));
    //prints -1
}
