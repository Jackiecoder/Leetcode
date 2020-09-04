# include <iostream>
# include <vector>
using namespace std;
   
int main(){
    return 0;
}
 
bool search(vector<int>& nums, int target) {
    int l = 0, mid;
    auto r = nums.size() - 1;
    if (r == -1){
        return false;
    }
    while (l + 1 < r){
        mid = l + (r - l) / 2;
        if (nums[mid] == target) return true; 
        while (l < mid && nums[l] == nums[mid]){
            l += 1;
        }
        if (nums[l] <= nums[mid]){
            if (nums[l] <= target && target < nums[mid]){
                r = mid;
            }else {
                l = mid;
            }
        }else{
            if (nums[mid] < target && target <= nums[r]) {
                l = mid;
            }else {
                r = mid;
            }
        }
    }
    if (nums[l] == target || nums[r] == target) return true;
    return false;
}
