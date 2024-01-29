// Q2: Explain the behavior of the three code fragments.  In each case the input is line one\nline two\m
#include <stdio.h>

int main() {
char s1[10];
fgets(s1, 10, stdin); //safest of the three options, reads 10 characters from standard input
printf("%zu", strlen(s1));

char s2[10];
scanf("%9s", s2); //reads 9 characters.  The s in the format specifier reads strings
printf("%zu", strlen(s2));

char s3[10];
scanf("%10c", s3); //reads 10 characters.  The c in the format specifier reads characters
printf("%zu", strlen(s3));
}