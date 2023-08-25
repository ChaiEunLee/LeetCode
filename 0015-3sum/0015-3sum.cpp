class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int target = 0;
        sort(nums.begin(), nums.end());
        set<vector<int>> s;
        vector<vector<int>> output;
        for (int i=0; i<nums.size(); i++){
            int j = i+1;
            int k = nums.size()-1;
            while (j<k){
                int sum = nums[i] + nums[j] + nums[k];
                if (sum == target){
                    s.insert({nums[i], nums[j], nums[k]});
                    j++;
                    k--;
                } else if (sum < target){
                    j++;
                } else {
                    k--;
                }
            }
        }
        
        // s에 있는 element들이 triplets에 복사돼서 하나씩 출력되는데 타입을 auto로 자동인식되도록 함
        for(auto triplets : s)
            output.push_back(triplets);
        return output;
    }
};