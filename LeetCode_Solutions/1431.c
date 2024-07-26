/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdlib.h>
#include <stdbool.h>

bool* kidsWithCandies(int* candies, int candiesSize, int extraCandies, int* returnSize) {

    int res = 0;
    bool t = true;
    bool f = false;
    bool* result = (bool*)malloc(candiesSize * sizeof(bool));
    
  
    for (int i = 0; i < candiesSize; i++) { 
        if (res < candies[i]) {
            res = candies[i]; 
        }    
    }

    for (int i = 0; i < candiesSize; i++) { 
        if (candies[i] + extraCandies >= res) {
            result[i] = t;
        }   else {
            result[i] = f;
        }
    } 
    *returnSize = candiesSize;
    return result;
}