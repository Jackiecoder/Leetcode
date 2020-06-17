class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # use max heap to make sure most frequent task will excute first
        task_to_count = collections.Counter(tasks)
        heap = [(-value, key) for key, value in task_to_count.items()]
        heapq.heapify(heap)
        cur_time = 0
        while heap:
            # find out how many tasks can be done in one cooling interval n
            i, excuted_task = n + 1, []
            while i > 0 and heap:
                neg_val, key = heapq.heappop(heap)
                neg_val += 1
                i -= 1
                if neg_val != 0:
                    excuted_task.append((neg_val, key))
                cur_time += 1
            # print(cur_time, excuted_task, heap)
            if not excuted_task and not heap:
                break
            cur_time += i
            heap.extend(excuted_task)
            heapq.heapify(heap)
        return cur_time
