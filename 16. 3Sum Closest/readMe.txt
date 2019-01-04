
This problem is about get 3 sum of three num in a list close to 'target' number.

In this problem, we first assume first three nums are our result, then there will be two conditions:
    1. the list only have 3 nums. 
    2. the list have more than 3 nums, and maybe exist better result.
For condition 1, we compare j='0+1' with k='len(List)-1'. if len==3, have j == k, we can just output the result.
For condition 2, 
        |||||||||||||||||||||||
           i  j-->        <--k
           ->
we set i, and move j and k. When result is lower than target, we improve it by increase j; and when result is larger than target, we decline it by decrease k.