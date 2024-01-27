// Q2: Explain the behavior of the three code fragments.  In each case the input is line one\nline two\m
#include <stdio.h>

int main() {
char s1[10];
fgets(s1, 10, stdin);
printf("%zu", strlen(s1));

char s2[10];
scanf("%9s", s2);
printf("%zu", strlen(s2));

char s3[10];
scanf("%10c", s3);
printf("%zu", strlen(s3));
}