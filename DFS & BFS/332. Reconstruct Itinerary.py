class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # use stack to solve it
        # post-order travel through + backtracking
        # *** This is a really amazing algorithm ***
        # make a graph that each departure is the root, and the arrival are sorted lexically as the children
        # we want to reach its lexical smallest child first
        # so we reach (root), (left), (right) order
        # The tricky part is that what if the left child is not the correct path?
        # e.g. a->c->a->b
        # In this example, we need to reach c first, then b, but if we travel through by lexical, we will reach b first. So we can't push b to our result first
        graph = defaultdict(list)
        for departure, arrival in tickets:
            graph[departure].append(arrival)
        for departure in graph.keys():
            graph[departure] = sorted(graph[departure], reverse=True)
        stack = ['JFK']
        res = []
        while stack:
            top = stack[-1]
            if top in graph and graph[top]:
                next_arrival = graph[top].pop()
                stack.append(next_arrival)
            else:
                res.append(stack.pop())
        return res[::-1]

    def findItinerary_backtracking(self, tickets: List[List[str]]) -> List[str]:
        # 1. visit all departure and arrival in the tickets
        # -> BFS or DFS to do it
        # 2. compare BFS and DFS.
        # -> because ticket are need to choose by lexical order
        #   thus if we use BFS we will need to store all of the possible path
        #   but if we use DFS, once we have a valid path, we can end the search
        # e.g.
        #     JFK
        #   /.    \
        # ATL      SFO
        # /  \
        # JFK SFO
        # Time O(n), space O(n)

        tickets_dict = defaultdict(list)
        for departure, arrival in tickets:
            tickets_dict[departure].append(arrival)
        for key, val in tickets_dict.items():
            tickets_dict[key] = sorted(val)
        res = []
        self.find(tickets_dict, ['JFK'], 'JFK', res)
        return res

    def find(self, tickets_dict, path, cur_loc, res):
        # this function will return True if the path is found
        if not tickets_dict:
            res[:] = path
            return True
        if cur_loc not in tickets_dict:
            return False

        arrival_ls = tickets_dict[cur_loc][:]
        for i, arrival in enumerate(arrival_ls):
            if i > 0 and arrival == arrival_ls[i - 1]:
                continue
            tickets_dict[cur_loc].pop(i)
            if not tickets_dict[cur_loc]:
                tickets_dict.pop(cur_loc)
            path.append(arrival)
            if self.find(tickets_dict, path, arrival, res):
                return True
            tickets_dict[cur_loc][:] = arrival_ls
            path.pop()
        return False
