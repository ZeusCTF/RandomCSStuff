// Q1: Explain what the program below does?
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <unistd.h>
#include <string.h>

#define MAX_BUF_SIZE 256

int main() {
    const char* home;
    char command[MAX_BUF_SIZE];
    int len = 0;

    home = getenv("HOME");
    if (home == NULL){/*handle error and exit*/ }

    len = snprintf(command, sizeof(command),
                            "%s%s%s", "ls -l ", home, " | head -n 5");
    if (len >= MAX_BUF_SIZE || len < 0) {/*handle error and exit*/ }
    
    system(command);

    return 0;
}

/*
This program first checks to see if the HOME directory is set in the local environment variables, then if so, runs the "ls" command and pipes it to "head" to gather the first few items from the output of ls
*/