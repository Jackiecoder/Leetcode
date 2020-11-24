class SparseVector
{
public:
    vector<pair<int, int>> vec;
    SparseVector(vector<int> &nums)
    {
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] == 0)
                continue;
            vec.push_back(pair(i, nums[i]));
        }
    }

    // Return the dotProduct of two sparse vectors
    int dotProduct(SparseVector &sv)
    {
        int res = 0;
        for (int i = 0, j = 0; i < vec.size() && j < sv.vec.size();)
        {
            auto [p1, n1] = vec[i];
            auto [p2, n2] = sv.vec[j];
            if (p1 > p2)
            {
                j++;
            }
            else if (p1 < p2)
            {
                i++;
            }
            else
            {
                res += n1 * n2;
                i++, j++;
            }
        }
        return res;
    }
};

// Your SparseVector object will be instantiated and called as such:
// SparseVector v1(nums1);
// SparseVector v2(nums2);
// int ans = v1.dotProduct(v2);