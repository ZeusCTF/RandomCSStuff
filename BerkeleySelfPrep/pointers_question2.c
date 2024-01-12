//Q2: What does the following program print when run with the arguments: one two three?
#include <stdio.h>

int main(int argc, char *argv[])
{
    for (char *p; p = *++argv;)
        for (; *p; ++p)
            putchar(*p);
} //prints to stdout the arguements provided prior to runtime.  In this case, it would be onetwothree