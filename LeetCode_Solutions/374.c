/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

#include <math.h>

int guessNumber(int n){
	int x = n / 2;
    int y;

    x = round(x);
    y = guess(x);


    while (y != 0) {
        if (y == -1){
            x = x / 2;
            guess(x);
        } else if (y == 1)
        {
            x = (x + n) / 2;
            guess(x);
        }
        
        
    }

}