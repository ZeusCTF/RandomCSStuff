#include <string.h>

int scoreOfString(char* s) {
    int res = 0;
    size_t i;

    for (i = 0; i < strlen(s); i++) {
        res += s[i];
}   return res; }