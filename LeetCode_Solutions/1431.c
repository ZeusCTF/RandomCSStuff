/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
kidsWithCandies(int* candies, int candiesSize, int extraCandies, int* returnSize) {

    int res = 0;
    char* t = "true";
    char* f = "false";
    int array[candiesSize];
    
  
    for (int i = 0; i < candiesSize; i++) { 
        if (res < candies[i]) {
            res = candies[i]; 
        }    
    }

    for (int i = 0; i < candiesSize; i++) { 
        if (candies[i] + extraCandies >= res) {
            array[i] = t;
        }   else {
            array[i] = f;
        }
    } return array;
}