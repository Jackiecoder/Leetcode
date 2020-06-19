class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # BFS
        # do bfs from each building, and get distance of each empty land.
        #  [[1,1,1,1,1],
        #   [2,2,2,2,2],
        #   [0,0,0,0,0]]

        # for (0, 0)
        #  [[-1,1,-1,5,-1],
        #   [1,2,3,4,5],
        #   [2,3,-1,5,6]]

        # [[-1, 5, -1, 1, 0],
        # [5, 4, 3, 2, 1],
        # [-1, 5, -1, 3, 2]]

        # [[-1, 3, -1, 3, -1],
        # [3, 2, 1, 2, 3]
        # [2, 1, 0, 1, 2]]

        # place should not be [building] or [block]
        # go through the grid, and make building and obstacle to -1
        # record all buildings
        # for building in buildings:
        #   use bfs to get how many steps will need for each place
        # queue = [(0, 1), (1, 0)]
        # building = [(0, 0), (0, 4), (2, 2)]
        # time O(kmn), space O(mn)

        m, n = len(grid), len(grid[0])
        sum_grid = [[0] * n for _ in range(m)]
        reach_building_grid = [[0] * n for _ in range(m)]
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        buildings = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 or grid[i][j] == 2:
                    sum_grid[i][j] = -1
                    if grid[i][j] == 1:
                        buildings.append((i, j))

        for building in buildings:
            queue = collections.deque([building])
            visited = set([building])
            reach_building = set([building])
            step = 1
            while queue:
                for _ in range(len(queue)):
                    x, y = queue.popleft()
                    for delta_x, delta_y in direction:
                        new_x, new_y = x + delta_x, y + delta_y
                        if (new_x, new_y) in buildings and (new_x, new_y) not in reach_building:
                            reach_building.add((new_x, new_y))
                            continue
                        if 0 <= new_x < m and 0 <= new_y < n and sum_grid[new_x][new_y] != -1 and (new_x, new_y) not in visited:
                            sum_grid[new_x][new_y] += step
                            reach_building_grid[new_x][new_y] += 1
                            queue.append((new_x, new_y))
                            visited.add((new_x, new_y))
                step += 1
            # check all building are visited
            if len(buildings) != len(reach_building):
                return -1

        min_steps = float('INFINITY')
        for i in range(m):
            for j in range(n):
                if reach_building_grid[i][j] == len(buildings) and sum_grid[i][j] > 0:
                    min_steps = min(min_steps, sum_grid[i][j])
        if min_steps == float('INFINITY'):
            return -1
        return min_steps
