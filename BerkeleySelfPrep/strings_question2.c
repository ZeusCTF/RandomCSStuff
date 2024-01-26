// Q2: What does the call to len2() produce?
#include <stdio.h>
#include <string.h>

void len1(char s[]) {
printf("size: %zu, len: %zu\n", sizeof(s), strlen(s)); //size 8, len 3 -> this is because the array is passed as a pointer, not the actual size
}

int main() {
char s[10] = "foo";
printf("size: %zu, len: %zu\n", sizeof(s), strlen(s)); //size 10, len 3
len1(s);
};