// Q2: What output does the following code produce?

void initArray() {
    int array[3];
    int i = 3, x = 3;

    while (--i && (array[i] = --x))
          printf("%d\n", array[i]);
}