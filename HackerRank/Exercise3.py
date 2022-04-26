from bisect import bisect_left
from collections import Counter

def climbingLeaderboard(ranked, player):
    # Write your code here
    counts = Counter(ranked)
    counts = sorted(counts)
    n = len(counts)
    lst = []

    for pr in player:
        i = bisect_left(counts, pr)
        if i < n and counts[i] == pr:
            lst.append(n-i)
        else:
            lst.append(n+1-i)
    return lst


if __name__ == '__main__':
    ranked = [100, 100, 50, 40, 40, 20, 10]
    player = [5, 25, 50, 120]

    climbingLeaderboard(ranked, player)