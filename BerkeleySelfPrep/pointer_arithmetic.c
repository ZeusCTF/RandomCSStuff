// Q1: What does the following function do?

char *foo(char *restrict d, const char *restrict s)
{
    const unsigned char *s_tmp = s;
    unsigned char *d_tmp = d;
    while ((*d_tmp++ = *s_tmp++));
    return d;
}