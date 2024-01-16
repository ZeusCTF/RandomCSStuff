//Q2: What does the following code print?
#include <stdio.h>

int main() {
    struct {
    char s[3];
    int i;
    } x;

    printf("%d\n", (char *)&x.i - x.s);
    printf("%d\n", sizeof(x) - sizeof(x.s) - sizeof(x.i));

}
