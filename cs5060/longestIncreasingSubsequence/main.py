def longest_increasing_subsequence(A):
    n = len(A)
    lis_length = [1] * n
    previous_index = [-1] * n

    for i in range(n):
        for j in range(i):
            if A[j] < A[i] and lis_length[j] + 1 > lis_length[i]:
                lis_length[i] = lis_length[j] + 1
                previous_index[i] = j

    max_length = max(lis_length)
    end_index = lis_length.index(max_length)

    longest_subsequence = []
    while end_index != -1:
        longest_subsequence.append(A[end_index])
        end_index = previous_index[end_index]

    return max_length, longest_subsequence[::-1]

# Example usage:
A = [5, 12, 4, 14, 5, 19, 22, 6, 7, 9, 15, 19]
length, subsequence = longest_increasing_subsequence(A)
print("Length of longest increasing subsequence:", length)
print("Longest increasing subsequence:", subsequence)



def can_fit_subset(n, M, size):
    # Initialize the 2D array with dimensions (n + 1) x (M + 1)
    array = [[False] * (M + 1) for _ in range(n + 1)]

    # Initialize the first column of array to be true
    for i in range(n + 1):
        array[i][0] = True

    # Iterate through each item and sum
    for i in range(1, n + 1):
        for j in range(1, M + 1):
            # Check if array[i-1][j] is true
            if array[i - 1][j]:
                array[i][j] = True
            elif j >= size[i - 1]:
                # Check if array[i-1][j-size[i]] is true
                if array[i - 1][j - size[i - 1]]:
                    array[i][j] = True

    # Check if array[n][M] is true
    return array[n][M]

# Example usage:
n = 4
M = 14
sizes = [2, 7, 9, 3]  # Sizes of items

can_fit = can_fit_subset(n, M, sizes)
print()
print(f"Can a subset fit in a knapsack of size {M} perfectly? {can_fit}")





def fib(n, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n == 1 or n == 2:
        return 1

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]




print(fib(5))









graph = {
    1: [(2, 'blue'), (3, 'red')],
    2: [(1, 'blue'), (3, 'blue'), (4, 'red')],
    3: [(1, 'red'), (2, 'blue'), (4, 'red')],
    4: [(2, 'red'), (3, 'red')]
}

from collections import defaultdict

def find(spanning_tree, node):
    if spanning_tree[node] != node:
        spanning_tree[node] = find(spanning_tree, spanning_tree[node])
    return spanning_tree[node]


def union(spanning_tree, rank, x, y):
    x_root = find(spanning_tree, x)
    y_root = find(spanning_tree, y)
    if rank[x_root] < rank[y_root]:
        spanning_tree[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        spanning_tree[y_root] = x_root
    else:
        spanning_tree[y_root] = x_root
        rank[x_root] += 1


def kruskal_mst(graph):
    edges = []
    for u, adj in graph.items():
        for v, color in adj:
            edges.append((u, v, color))

    edges.sort(key=lambda x: (x[2] == 'red', x))

    spanning_tree = {node: node for node in graph}
    rank = defaultdict(int)

    mst_edges = []
    for u, v, color in edges:
        if find(spanning_tree, u) != find(spanning_tree, v):
            mst_edges.append((u, v, color))
            union(spanning_tree, rank, u, v)

    return mst_edges

mst = kruskal_mst(graph)
print('\n')
print(mst)





# graph = {
#     1: [(2, 'blue'), (3, 'red')],
#     2: [(1, 'blue'), (3, 'blue'), (4, 'red')],
#     3: [(1, 'red'), (2, 'blue'), (4, 'red')],
#     4: [(2, 'red'), (3, 'red')]
# }

# graph = {
#     1: [(2, 'blue'), (3, 'red'), (5, 'blue')],
#     2: [(1, 'blue'), (3, 'blue'), (4, 'red'), (5, 'red')],
#     3: [(1, 'red'), (2, 'blue'), (4, 'red'), (6, 'blue')],
#     4: [(2, 'red'), (3, 'red'), (6, 'blue')],
#     5: [(1, 'blue'), (2, 'red'), (6, 'red')],
#     6: [(3, 'blue'), (4, 'blue'), (5, 'red')]
# }