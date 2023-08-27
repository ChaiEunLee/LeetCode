int trap(int* height, int heightSize){
    int *L = height, *R = L+heightSize-1, level = 0, water = 0;
    while (L < R) {
        int lower = *L < *R ? *L++ : *R--;
        //printf("%d,%d,%d,%d\n", lower, level, *L, *R);
        if (lower > level) level = lower;
        water += level - lower;
    }
    return water;
}