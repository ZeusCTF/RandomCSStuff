/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
kidsWithCandies(int* candies, int candiesSize, int extraCandies, int* returnSize) {

    int res = malloc(candies[0]);
    
  
    for (int i = 0; i < candiesSize; i++) { 
        if (res < candies[i]) {
            res = candies[i]; 
        }    
    }

    for (int i = 0; i < candiesSize; i++) { 
        if (candies[i] + extraCandies >= res) {
            
        }    
    }
}