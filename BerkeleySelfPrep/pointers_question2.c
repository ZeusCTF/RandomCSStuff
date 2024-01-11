//Q2: What does the following program print when run with the arguments: one two three?

int main(int argc, char *argv[])
{
    for (char *p; p = *++argv;)
        for (; *p; ++p)
            putchar(*p);
}