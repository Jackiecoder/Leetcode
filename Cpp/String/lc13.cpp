class Solution
{
public:
    int romanToInt(string s)
    {
        // add each char, when previous char < current char, minus 2 * previous char
        unordered_map<char, int> roman_to_int = {{'M', 1000}, {'D', 500}, {'C', 100}, {'L', 50}, {'X', 10}, {'V', 5}, {'I', 1}};
        int res = 0, previous = 0, cur = 0;
        for (int i = 0; i < s.size(); i++)
        {
            cur = roman_to_int[s[i]];
            if (cur > previous)
                res -= previous * 2;
            res += cur;
            previous = cur;
        }
        return res;
    }
};