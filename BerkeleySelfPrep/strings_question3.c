// Q3: What is the result of running the following program?
#include <stdio.h>
#include <string.h>

int main() {
    char arr[] = "abcc";
    char *str = "abcc";

    *(arr + 3) = 'd';
    puts(arr);
    *(str + 3) = 'd';
    puts(str);

    return 0;
}