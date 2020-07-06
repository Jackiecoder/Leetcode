'''
Quick select can be used to choose the Kth element, 
or choose top K elements regardless the order.
'''
import random
# 1. choose Kth smallest elements
# 2. choose top K smallest elements


def Kth(tc, k):
    quick_select(tc, 0, len(tc) - 1, k)
    return tc[k]


def top_k(tc, k):
    quick_select(tc, 0, len(tc) - 1, k)
    return tc[:k]


def quick_select(tc, start, end, k):
    if start >= end:
        return
    p = partition(tc, start, end)
    if p == k:
        return
    elif p < k:
        return quick_select(tc, p + 1, end, k)
    else:
        return quick_select(tc, start, p - 1, k)


def partition(tc, start, end):
    pivot = tc[end]
    greater = start
    for i in range(start, end):
        if tc[i] <= pivot:
            tc[i], tc[greater] = tc[greater], tc[i]
            greater += 1
    tc[greater], tc[end] = tc[end], tc[greater]
    return greater


def testcase_creation(length, left_range, right_range):
    return [random.randint(left_range, right_range) for _ in range(length)]


def varify_function_kth(tc, k, res):
    return sorted(tc)[k] == res


def varify_function_topK(tc, k, res):
    return set(sorted(tc)[:k]) == set(res)


tc = testcase_creation(100, 0, 1000)
k = 88
res = Kth(tc, k)
print(varify_function_kth(tc, k, res))
res = top_k(tc, k)
print(varify_function_topK(tc, k, res))
