class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # dfs
        # time O(n), space O(n)
        dic = collections.defaultdict(list)
        for ticket in tickets:
            dic[ticket[0]].append(ticket[1])
        for departure in dic:
            dic[departure].sort(reverse=True)

        stack = ['JFK']
        res = []
        while stack:
            top = stack[-1]
            if top in dic and len(dic[top]) > 0:
                stack.append(dic[top].pop())
            else:
                res.append(stack.pop())
        return res[::-1]
