// Q1: Assuming that the function printString prints the string it receives as an argument one character at a time.  What is the output of the following program?
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int main() {

    pid_t pid;
    pid = fork();
    if (pid) {
        printString("Hello\n");
    }
    else {
        printString("World!\n");
    }
} 

/* This program will print the characters for each word at the same tim.  For example:
H
W
e
o
l
r
...
*/