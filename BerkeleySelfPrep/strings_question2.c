// Q2: What does the call to len2() produce?

void len1(char s[]) {
printf("size: %zu, len: %zu\n", sizeof(s), strlen(s));
}

void len2(void) {
char s[10] = "foo";
printf("size: %zu, len: %zu\n", sizeof(s), strlen(s));
len1(s);
}