/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getConcatenation(int* nums, int numsSize, int* returnSize) {
    int* arrayPtr = (int *)malloc((2 * numsSize) * sizeof(int));

    for (int i = 0; i < numsSize; i++) {
        arrayPtr[i] = nums[i];
        arrayPtr[i + numsSize] = nums[i];
    }

    *returnSize = 2 * numsSize;

    return arrayPtr;
}