class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # BFS
        # time complexity
        # = n * C(n,n) + (n-1)*C(n,n-1) + (n-2)*C(n,n-2) + ...
        # = n * (2**n)
        # time O(2**n)
        res = []
        if not s:
            return [""]
        visited = set([s])
        queue = deque([s])
        found = False
        while queue:
            s = queue.popleft()
            if self.isValid(s):
                res.append(s)
                found = True
            if found:
                continue
            # if not found any valid answer, try to remove one parenthese and push the new string to queue.
            # if already found one valid answer, means all of our answer should be in the queue. we don't need to continue remove any characters from the string.
            for i, char in enumerate(s):
                if char != '(' and char != ')':
                    continue
                new_s = s[:i] + s[i + 1:]
                if new_s not in visited:
                    queue.append(new_s)
                    visited.add(new_s)
        return res

    def isValid(self, s):
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0
