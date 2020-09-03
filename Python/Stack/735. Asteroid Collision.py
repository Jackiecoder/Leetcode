class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # each asteroid, if val > 0 -> push to stack
        #                if val < 0 -> pop stack, push which have larger absolute, if same: continue

        stack = collections.deque()
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                destoryed = False
                while stack and stack[-1] > 0:
                    top = stack.pop()
                    if asteroid + top >= 0:
                        if asteroid + top > 0:
                            stack.append(top)
                        destoryed = True
                        break
                if not destoryed:
                    stack.append(asteroid)
        return stack
