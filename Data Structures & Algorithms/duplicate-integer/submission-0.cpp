class Solution {
    public:
        bool hasDuplicate(vector<int>& nums) {
            set<int> duplicates;

            for (int num: nums) {
                if (duplicates.count(num)) {
                    return true;
                }
                duplicates.insert(num);
            }
            return false;
        }
};
