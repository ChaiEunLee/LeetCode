/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize){
    int *result;
    int l, r, total;

    result = malloc(2 * sizeof(int)); // int 2개를 return 할거니까 malloc으로 확보  
    //assert(result);

    *returnSize = 0;

    l = 0;
    r = numbersSize - 1;

    while (l < r) {
        total = numbers[l] + numbers[r];
        if (total > target) {
            r --;
        } else if (total < target) {
            l ++;
        } else {
            result[0] = l + 1; // index가 0 부터 시작하니까 몇번째인지는 +1
            result[1] = r + 1; // index가 0 부터 시작하니까 몇번째인지는 +1
            *returnSize = 2; // 이건 왜해주는거지?.. 모르겠다.
            break;
        }
    }
    return result;
}