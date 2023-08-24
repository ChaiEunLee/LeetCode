#include <stdio.h>

int removeDuplicates(int* nums, int numsSize){
    int uniqcnt=0;
    for (int i=0; i<numsSize; i++){
        if (ifDup(nums, numsSize, i, nums[i])){
            nums[uniqcnt] = nums[i];
            uniqcnt++;
        }
    }   
    return uniqcnt;
}

int ifDup(int* nums, int numsSize, int k, int value){
    for (int i=0; i<k; i++){
        if (nums[i] == value){
            return 0;
        }
    }
    return 1;
}