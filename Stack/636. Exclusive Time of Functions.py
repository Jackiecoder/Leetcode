class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        # Hash table 1 to store {id: start time}
        # hash table 2 to store {id: exclusive time}
        # return sorted key from hashtable 1
        stack = []
        id_time = collections.defaultdict(int)
        prev_time = 0
        for log in logs:
            id, action, time = log.split(':')
            id, time = int(id), int(time)
            if action == 'start':
                if stack:
                    # other id is executing
                    id_time[stack[-1]] += time - prev_time
                stack.append(id)
                prev_time = time
            else:
                # when end, id === stack peek
                id_time[id] += time - prev_time + 1
                prev_time = time + 1
                stack.pop()
        return [id_time[k] for k in sorted(id_time.keys())]
