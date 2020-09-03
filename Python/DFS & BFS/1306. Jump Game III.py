class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # dfs
        # use a stack to solve it
        # Time O(n), space O(n)

        visited = set()
        stack = [start]
        while stack:
            cur = stack.pop()
            if arr[cur] == 0:
                return True
            left = cur - arr[cur]
            if 0 <= left < len(arr) and left not in visited:
                stack.append(left)
                visited.add(left)
            right = cur + arr[cur]
            if 0 <= right < len(arr) and right not in visited:
                stack.append(right)
                visited.add(right)
        return False
