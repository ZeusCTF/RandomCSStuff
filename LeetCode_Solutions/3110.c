#include <string.h>
#include<stdlib.h>

int scoreOfString(char* s) {
    int res = 0;
    int x = 0;
    int y = 1;
    size_t i;

    while (y < strlen(s)) {
        res += abs(s[x] - s[y]);
        y++;
        x++;
}   return res; }