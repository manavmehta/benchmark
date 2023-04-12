def mean(arr):
    return sum(arr)/len(arr)

def p50(arr):
    sorted_list = sorted(arr)
    n = len(sorted_list)

    if n % 2 == 0:
        p50 = (sorted_list[n//2-1] + sorted_list[n//2]) / 2
    else:
        p50 = sorted_list[n//2]
    return p50

def p10(arr):
    sorted_list = sorted(arr)
    # print(sorted_list)
    n = len(sorted_list)

    p10_index = int(n * 10 / 100)
    p10 = sorted_list[p10_index]
    return p10

def p90(arr):
    sorted_list = sorted(arr)
    # print(sorted_list)
    n = len(sorted_list)

    p90_index = int(n * 90 / 100)
    p90 = sorted_list[p90_index]
    return p90
