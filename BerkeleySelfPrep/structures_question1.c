//Q1: What is the output when running the following program?
#include <stdio.h>

struct Date
{
    int day;
    int month;
    int year;

};
 
int main()
{
    struct Date d = { 1, 1, 2020 };

    struct Date *d2;
    d2 = &d;

    printf("%d/%d/%d\n", d2->day, d2->month, d2->year);
}
/*
This code creates a struct d, and initializes a pointer to the created struct, d2.  Then uses the d2 pointer to refer to the contents within d, outputting 1/1/2020
*/