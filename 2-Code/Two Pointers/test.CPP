#include <bits/stdc++.h>
#include <algorithm>
using namespace std;

int main(){
    class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            int i = 0, j = nums.size()-1;
            sort(nums.begin(), nums.end());
            while(i < j) {
                if (nums[i] + nums[j] == target){
                    return {i,j};
                } else if (nums[i] + nums[j] > target) {
                    j--;
                } else {
                    i++;
                }
            }
            return {-1, -1};
        }
    };
    Solution s;
    vector<int> nums = {2,3,4,5,7,9};
    vector<int> d = s.twoSum(nums,9);
    for (int i = 0; i < int(d.size()); i++) {
        cout << d[i] <<endl;
    }
    getchar();
    return 0;
}