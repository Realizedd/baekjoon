
dir_anticlockwise = {
    'N': 'W',
    'W': 'S',
    'S': 'E',
    'E': 'N'
}
dir_move = {
    'N': (-1, 0),
    'E': (0, 1),
    'S': (1, 0),
    'W': (0, -1)
}

args = input().split(' ')
N, M = int(args[0]), int(args[1])
grid = []
walls, cctvs = 0, 0

class CCTV:
    def __init__(self, location, directions) -> None:
        self.location = location
        self.directions = directions
        self.watching = set()

    def rotate(self):
        for i in range(len(self.directions)):
            self.directions[i] = dir_anticlockwise[self.directions[i]]
        
    def clear(self, idx, watching):
        for location in self.watching:
            watching[location].remove(idx)
        
        self.watching = set()

    def trace(self, idx, watching):
        for direction in self.directions:
            location = self.location

            while True:
                move = dir_move[direction]
                new_location = (location[0] + move[0], location[1] + move[1])

                if new_location[0] not in range(N) or new_location[1] not in range(M) or grid[new_location[0]][new_location[1]] == 6:
                    break
                
                if grid[new_location[0]][new_location[1]] == 0:
                    watching[new_location].add(idx)
                    self.watching.add(new_location)
                
                location = new_location

watchers = []

for r in range(N):
    row = list(map(int, input().split(' ')))
    grid.append(row)

    for c in range(M):
        if 0 < grid[r][c] < 6:
            cctvs += 1
        if grid[r][c] == 1:
            watchers.append(CCTV((r, c), ['E']))
        if grid[r][c] == 2:
            watchers.append(CCTV((r, c), ['E', 'W']))
        if grid[r][c] == 3:
            watchers.append(CCTV((r, c), ['E', 'N']))
        if grid[r][c] == 4:
            watchers.append(CCTV((r, c), ['E', 'W', 'N']))
        if grid[r][c] == 5:
            watchers.append(CCTV((r, c), ['E', 'W', 'N', 'S']))
        if grid[r][c] == 6:
            walls += 1

def exhaustive_search(idx, watching):
    if idx >= len(watchers):
        total = 0

        for k in watching:
            if watching[k]:
                total += 1
        
        # for r in range(N):
        #     for c in range(M):
        #         print(9 if (r,c) in watching and watching[(r,c)] else grid[r][c], end=' ')
        #     print()
        
        # print(N * M - total - cctvs - walls)
        return N * M - total - cctvs - walls
    
    watchers[idx].trace(idx, watching)
    res = exhaustive_search(idx + 1, watching)
    watchers[idx].clear(idx, watching)
    
    for _ in range(3):
        watchers[idx].rotate()
        watchers[idx].trace(idx, watching)
        res = min(res, exhaustive_search(idx + 1, watching))
        watchers[idx].clear(idx, watching)

    return res

watching = {}

for r in range(N):
    for c in range(M):
        watching[(r,c)] = set()

print(exhaustive_search(0, watching))
