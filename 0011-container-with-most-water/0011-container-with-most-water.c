int maxArea(int* height, int heightSize){
    int i = 0;
    int j = heightSize-1;
    int water = 0;
    int minheight = 0;

    while(i<j){
        minheight = (height[i]<height[j]) ? height[i] : height[j];
        water = (water<(minheight)*(j-i)) ? (minheight)*(j-i) : water;
        if (height[i]<height[j]){
            i++;
        } else {
            j--;
        }
    }
    return water;
}
