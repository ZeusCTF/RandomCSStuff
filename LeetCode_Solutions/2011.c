int finalValueAfterOperations(char** operations, int operationsSize) {
    int res = 0;
    char str1[] = "X++";
    char str2[] = "++X";

    for (int i = 0; i < operationsSize; i++){
        if (strcmp(operations[i], str1) == 0 || strcmp(operations[i], str2) == 0) {
            res++;
        } else {
            res--;
        }
    } return res;
}