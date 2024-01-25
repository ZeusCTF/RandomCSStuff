// Q1: What is the output of the following program?
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {

    char *t;
    const char *str = "item1 item2 item3 item4 item5"; //declares a pointer to a constant string 'str' variable

    char *tmp = (char *)malloc(strlen(str) + 1); //allocates memory equal to match the str variable
    if (tmp == NULL) {
        exit(1);
    }
    strcpy(tmp, str);  //copies str into tmp
    t = strtok(tmp, " "); //splits a string based on a given delim.  So in this case, splits tmp based upon spaces
    printf("%s,", t); //prints the result as one contigious string

    while (t = strtok(0, " ")) {
        printf("%s,", t);
    }

    free(tmp); //deallocates memory
    tmp = NULL;
}