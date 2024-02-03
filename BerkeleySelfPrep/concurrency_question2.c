// Q2: What does the following program output?
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

int main() {
    pid_t childpid;
    int x = 0;

    childpid = fork();
    if (childpid == 0)
            x = x + 4;
    
    childpid = fork();
    if (childpid == 0)
            x = x + 2;

    childpid = fork();
    if (childpid == 0)
            x = x + 1;

    printf("%d", x);
}
//  My assumption here was that the program would output 14, however upon testing, the program is outputting 12
//