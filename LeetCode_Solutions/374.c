/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */
#include <math.h>

//int guess(int num);

int guessNumber(int n) {
    int lower = 1;
    int upper = n;
    int guessednum;
    int res;

    while (lower <= upper) {
        guessednum = lower + (upper - lower) / 2;
        res = guess(guessednum);

        if (res == 0) {
            return guessednum;
        } else if (res == 1) {
            lower = guessednum + 1;
        } else if (res == -1) {
            upper = guessednum - 1;
        }
    }
    return -1;
}