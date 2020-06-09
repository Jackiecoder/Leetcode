class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = collections.deque()
        for p in path.split('/'):
            if p == '..':
                if stack:
                    stack.pop()
            elif p and p != '.':
                stack.append(p)
        return '/' + '/'.join(stack)

        '''
        # many / -> one /
        # if . between two /, skip it
        # if .. between two /, drop last directory
        # stack store path
        # if while /, i --> 
        #   name = a
        #   if name == '.': do nothing
        #   elif name == '..':  pop stack
        #   else: stack.append(name)
        # recover: '/' + '/'.join(stack)
        # time O(n), space O(n)
        stack = collections.deque()
        index = 0
        n = len(path)
        while index < n:
            while index < n and path[index] == '/':
                index += 1
            name = ''
            while index < n and path[index] != '/':
                name = name + path[index]
                index += 1
            if name == '.':
                continue
            elif name == '..':
                if stack:
                    stack.pop()
            elif name:
                stack.append(name)
        return '/' + '/'.join(stack)
                '''
