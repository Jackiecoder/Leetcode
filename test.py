import collections


def droppedRequests(requestTime):
    '''
    [1,1,1,1, 100,100,100,100]
    lookup = {
        1: 4,
        100: 4
    }
    '''
    if len(requestTime) <= 3:
        return 0
    counter = collections.Counter(requestTime)
    drop = 0
    for time in sorted(counter):
        # 3 request in one second
        if counter[time] > 3:
            counter[time] = 3
        # find previous 10 sec
        tmp = 0
        for sec in range(9, -1, -1):
            tmp += counter.get(time - sec, 0)
            if tmp >= 10:
                counter[time] = 0
                break
        counter[time] = min(counter[time], 10 - tmp)
        # find previous 60 sec
        tmp = 0
        for sec in range(59, -1, -1):
            tmp += counter.get(time - sec, 0)
            if tmp >= 60:
                counter[time] = 0
                break
        counter[time] = min(counter[time], 60 - tmp)
    return len(requestTime) - sum(counter.values())


testcase = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7]
