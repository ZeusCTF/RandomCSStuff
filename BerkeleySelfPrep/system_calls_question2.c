// Q2: Explain what the program below does?
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <unistd.h>
#include <string.h>

extern char **environ;
int main() {
    if (setenv("PATH", "/some/path/bin", 1) != 0) {
        /* Handle error and exit */
    }
    if (environ != NULL) {
        for (size_t i = 0; environ[i] != NULL; ++i) {
            puts(environ[i]);
        }
    }
    return 0;
}

/*
This program is designed to set the PATH environment variable, then print all environment variables afterwards
*/