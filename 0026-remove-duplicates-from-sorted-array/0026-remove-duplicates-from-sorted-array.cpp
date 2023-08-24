class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int uniqcnt = 0;
        for (int i=0; i<nums.size(); i++){
            if (ifDup(nums[i], nums, i)){
                nums[uniqcnt] = nums[i];
                uniqcnt++;
            }
        }
        return uniqcnt;        
    }

    bool ifDup(int x, vector<int>& nums, int index){
        for(int i=0; i<index; i++){
            if(nums[i] == x){
                return false;
            } 
        }
        return true;
    }
};