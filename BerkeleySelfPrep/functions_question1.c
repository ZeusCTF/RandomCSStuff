//Q1: What happens in the following functions?

void swap1(int x, int y){
    int tmp = x;
    x = y;
    y = tmp;
}

void swap2(int &x, int &y){
    int tmp = *x;
    *x = *y;
    *y = tmp;
}
