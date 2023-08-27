class Solution {
public:
    int trap(vector<int>& height) {
        int volume = 0;
        int l = 0;
        int r = height.size()-1;
        int lmax = height[l];
        int rmax = height[r];

        while(l<r){
            lmax = max(height[l],lmax);
            rmax = max(height[r],rmax);
            if (lmax < rmax){
                volume += lmax - height[l];
                l++;
            } else {
                volume += rmax - height[r];
                r--;
            }
        }
        return volume;
    }
};