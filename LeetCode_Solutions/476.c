#include <stdio.h>

void bin(unsigned n)
{
    char c[];

    if (n > 1)
        bin(n / 2);

    c += n % 2;
    printf("%d", n % 2);
}

int main(void)
{
    bin(7);
    printf("\n");
    bin(4);
}