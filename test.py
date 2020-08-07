def largestSum(length: int, numbers: list):
    # 1. calculate the sum of arr[:i] and store the results
    summ = [0]
    cumulation = 0
    for number in numbers:
        cumulation += number
        summ.append(cumulation)

    max_diff = 0
    cur_smallest = float('inf')
    for val in summ:
        cur_smallest = min(cur_smallest, val)
        max_diff = max(max_diff, val - cur_smallest)
    print(str(max_diff))


length = int(raw_input())
numbers = raw_input().split(' ')
numbers = [int(number) for number in numbers]
largestSum(length, numbers)
