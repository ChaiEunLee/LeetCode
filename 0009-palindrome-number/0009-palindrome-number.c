#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool isPalindrome(int x){
    if (x<0 || x!=0 && x%10 == 0) {return false;} // x<0:negative, x!=0, x%10==0: cannot be a palindrome number. 첫번째 숫자가 0일수는 없으니까. 
    int check = 0;
    while(x>check){ // x>check 되기 전까지 하면 중간까지 온거
        check = check*10 + x %10;
        x/=10;
    }
    return (x==check || x==check/10);
}