def coverInterval(intervals: list, target: list) -> int:
    intervals.sort(key=lambda x: (x[0], x[1]))
    print(intervals)
    index = 0
    n = len(intervals)
    count = 0
    start, end = target[0], target[1]
    while index < n:
        if intervals[index][1] < target[0]:
            index += 1
        else:
            if target[0] > start:
                break
            while index < n and intervals[index][0] < start:
                end = max(end, intervals[index][1])
                index += 1
            if start != end:
                count += 1
                start = end
    if end < target[1]:
        return -1
    return count


intervals = {
    'case1': [[3, 6], [4, 5], [7, 10], [6, 9], [7, 12], [12, 17], [10, 13], [18, 22], [16, 18]]
}
targets = {
    'case1': [7, 22]
}
result = {
    'case1': 4
}

for key in intervals:
    print(coverInterval(intervals[key], targets[key]), result[key])
