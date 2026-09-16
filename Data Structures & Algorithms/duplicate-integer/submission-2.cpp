class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> dupSet;
        for(int num : nums){
            if(dupSet.contains(num)){
                return true;
            }
            dupSet.insert(num);
        }
        return false;
    }
};