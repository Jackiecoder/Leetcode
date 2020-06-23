class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # time O(nlogn), space O(1)
        if m * k > len(bloomDay):
            return -1
        possible_day = sorted(list(set(bloomDay)))
        left, right = 0, len(possible_day) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            day = possible_day[mid]
            bouquets = self.day_n_bloom(bloomDay, k, day)
            if bouquets < m:
                left = mid
            else:
                right = mid
        if self.day_n_bloom(bloomDay, k, possible_day[left]) >= m:
            return possible_day[left]
        return possible_day[right]

    def day_n_bloom(self, bloomDay, k, day):
        cur_flower, bouquets = 0, 0
        for flower in bloomDay:
            if flower <= day:
                # this flower is bloom
                cur_flower += 1
            else:
                cur_flower = 0
            if cur_flower >= k:
                # complete one bouquet
                cur_flower = 0
                bouquets += 1
        return bouquets

        '''
        # time O(nlog(max(bloomDay)))
        n = len(bloomDay)
        if m * k > n:
            return -1
        max_day = max(bloomDay)
        left, right = 0, max_day
        while left + 1 < right:
            mid = (left + right) // 2
            bouquets = self.day_n_bloom(bloomDay, mid, k)
            if bouquets < m:
                left = mid
            else:
                right = mid
        if self.day_n_bloom(bloomDay, left, k) >= m:
            return left
        return right
        
    def day_n_bloom(self, bloomDay, day, k):
        cur_flower, bouquets = 0, 0
        for flower in bloomDay:
            if flower <= day:
                # this flower is bloom
                cur_flower += 1
            else:
                cur_flower = 0
            if cur_flower >= k:
                # complete one bouquet
                cur_flower = 0
                bouquets += 1
        return bouquets
        '''
