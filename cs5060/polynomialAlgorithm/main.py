


import random

def packKnapsack(k,n):
    random.shuffle(n)
    counter = 0
    while True:
        result = []
        totalSum = 0
        for i in range(counter, len(n)):
            if n[i] + totalSum == k:
                totalSum += n[i]
                result.append(n[i])
            if n[i] + totalSum < k:
                totalSum += n[i]
                result.append(n[i])

        if totalSum < (k / 2):
            counter += 1
        else:
            break
    print(result)
    return result


# def packKnapsack(k, n):
#     random.shuffle(n)
#     result = []
#     totalSum = 0
#
#     for item in n:
#         if totalSum + item <= k:
#             totalSum += item
#             result.append(item)
#
#         if totalSum >= k / 2:
#             break
#
#     print(result)
#     return result



# print(result)
#     print(counter)
packKnapsack(20, [9.3, 24, 14, 5, 8, 17, 4.2])

packKnapsack(20, [1, 1, 1, 1, 1, 1, 20])