#import sys
#sys.stdin = open("input.txt", "r")

import heapq


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input())) for _ in range(N)]
    
    q = [(grid[0][0], (0, 0))]
    visited = set()
    distance = {}

    while q:
        dist, loc = heapq.heappop(q)

        if loc in visited:
            continue
        
        visited.add(loc)

        if loc == (N - 1, N - 1):
            print(f'#{test_case} {dist}')
            break
        
        for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_loc = (loc[0] + dir[0], loc[1] + dir[1])

            if new_loc[0] not in range(N) or new_loc[1] not in range(N):
                continue

            new_dist = dist + grid[new_loc[0]][new_loc[1]]
            cur_dist = distance[new_loc] if new_loc in distance else float('inf')

            if new_dist < cur_dist:
                distance[new_loc] = new_dist
                heapq.heappush(q, (new_dist, new_loc))
