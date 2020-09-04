class UnionFind2:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        self.max_rank = 1

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            # already in same set
            return False
        if self.rank[root_x] < self.rank[root_y]:
            # make root x to be highest rank
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        self.rank[root_x] = self.rank[root_x] + self.rank[root_y]
        self.max_rank = max(self.max_rank, self.rank[root_x])
        return True


class UnionFind1:
    def __init__(self):
        self.parent = {}
        self.rank = defaultdict(lambda: 1)
        self.max_rank = 1

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            # already in same set
            return False
        if self.rank[root_x] < self.rank[root_y]:
            # make root x to be highest rank
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        self.rank[root_x] = self.rank[root_x] + self.rank[root_y]
        self.max_rank = max(self.max_rank, self.rank[root_x])
        return True


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # find the smallest starter
        num_set = set(nums)
        max_streak = 0
        for num in nums:
            if num - 1 not in num_set:
                cur_streak = 1
                while num + 1 in num_set:
                    # Although there is a nested while loop, but the overall run time of all while loop will be O(n),
                    # Thus Time = O(n + n) = O(n)
                    num += 1
                    cur_streak += 1
                max_streak = max(max_streak, cur_streak)
        return max_streak

    def longestConsecutive_unionFind2(self, nums: List[int]) -> int:
        # Union find
        # combine continuous numbers into one set.
        # 1. travel through the nums
        # 2. for each num, -> find if (num-1) and (num+1) in the set
        #    if both -> combine
        #    if one side -> add num as child
        #    if none -> create a parent
        if not nums:
            return 0
        uf = UnionFind2(len(nums))
        val_to_index = {}
        for i, num in enumerate(nums):
            if num in val_to_index:
                continue
            if num - 1 in val_to_index:
                uf.union(i, val_to_index[num - 1])
            if num + 1 in val_to_index:
                uf.union(i, val_to_index[num + 1])
            val_to_index[num] = i
        return uf.max_rank

    def longestConsecutive_unionFind1(self, nums: List[int]) -> int:
        # Union find
        # combine continuous numbers into one set.
        # 1. travel through the nums
        # 2. for each num, -> find if (num-1) and (num+1) in the set
        #    if both -> combine
        #    if one side -> add num as child
        #    if none -> create a parent
        if not nums:
            return 0
        uf = UnionFind1()
        visited = set()
        for num in nums:
            # print('\n', num)
            if num - 1 in visited:
                uf.union(num, num - 1)
            if num + 1 in visited:
                uf.union(num, num + 1)
            visited.add(num)
        return uf.max_rank
