// Q1: What does the following program do?
#include <stdio.h>

int main(int argc, char **argv) {

    FILE *fp;
    int x = 0;
    int c;

    fp = fopen(argv[1], "r");

    if (!fp) {
        /*handle error and exit*/
    }

    for (c = getc(fp); c != EOF; c = getc(fp)) {
        if (c == '\n')
            x++;
    }
    fclose(fp);
    printf("%d\n", x);

    return 0;
}

/*
This program counts the number of newline characters found in the provided file.
*/