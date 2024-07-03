dir_move = {
    'N': (-1, 0),
    'E': (0, 1),
    'S': (1, 0),
    'W': (0, -1)
}

args = input().split(' ')
N, M = int(args[0]), int(args[1])

grid = []

for _ in range(N):
    grid.append(list(input().split(' ')))

class BlockGroup:
    
    def __init__(self, base_loc) -> None:
        self.base_loc = base_loc
        self.rainbow_cnt = 0
        self.blocks = [base_loc]

    def add_block(self, new_loc, block_type):
        if block_type == '' or block_type == '-1':
            return False
        
        if block_type == '0' or grid[self.base_loc[0]][self.base_loc[1]] == block_type:
            self.blocks.append(new_loc)

            if block_type != '0':
                if new_loc[0] < self.base_loc[0] or (new_loc[0] == self.base_loc[0] and new_loc[1] < self.base_loc[1]): # update base block if biggest row # (if equal, biggest col #)
                    self.base_loc = new_loc
            else:
                self.rainbow_cnt += 1

            return True
        return False
    
def apply_gravity(grid):
    for r in range(N - 2, -1, -1):
        for c in range(N):
            block_type = grid[r][c]
            
            if block_type == '' or block_type == '-1':
                continue
            
            height_to_fall = r

            while height_to_fall + 1 < N and grid[height_to_fall + 1][c] == '':
                height_to_fall += 1
            
            if height_to_fall > r:
                grid[height_to_fall][c] = block_type
                grid[r][c] = ''


def rotate_grid(grid):
    new_grid = []

    for c in range(N - 1, -1, -1):
        cur_grid = []

        for r in range(N):
            cur_grid.append(grid[r][c])
        
        new_grid.append(cur_grid)
    
    return new_grid


checked_normals = set()
checked_current = set()

def explore(normal_loc: tuple, group: BlockGroup):
    for dir in dir_move:
        move = dir_move[dir]
        new_loc = (normal_loc[0] + move[0], normal_loc[1] + move[1])

        if new_loc[0] not in range(N) or new_loc[1] not in range(N) or new_loc in checked_current:
            continue

        block_type = grid[new_loc[0]][new_loc[1]]

        if group.add_block(new_loc, block_type):
            checked_current.add(new_loc)

            if block_type != '0':
                checked_normals.add(new_loc)

            explore(new_loc, group)

score = 0

while True:
    groups = []
    largestGroup = None

    for r in range(N):
        for c in range(N):
            block_type = grid[r][c]
            if block_type != '' and block_type != '-1' and block_type != '0' and (r, c) not in checked_normals: # Normal block found and not already checked in this iteration
                checked_normals.add((r, c))

                checked_current.add((r, c))
                group = BlockGroup((r, c))
                explore((r, c), group) # Add all reachable normal/rainbow blocks to current group
                checked_current.clear()

                groupSize = len(group.blocks)
                groupRainbow = group.rainbow_cnt
                groupBase = group.base_loc

                if len(group.blocks) >= 2: # If group is at least size 2 or bigger
                    groups.append(group)

                    largestSize = 0 if not largestGroup else len(largestGroup.blocks)
                    largestRainbow = 0 if not largestGroup else largestGroup.rainbow_cnt
                    largestBase = None if not largestGroup else largestGroup.base_loc

                    if largestGroup == None or groupSize > largestSize or (groupSize == largestSize and (groupRainbow > largestRainbow or (groupRainbow == largestRainbow and (groupBase[0] > largestBase[0] or (groupBase[0] == largestBase[0] and groupBase[1] > largestBase[1]))))):
                        largestGroup = group

    if not groups:
        break

    score += len(largestGroup.blocks) ** 2

    for block_loc in largestGroup.blocks:
        grid[block_loc[0]][block_loc[1]] = ''

    apply_gravity(grid)
    grid = rotate_grid(grid)
    apply_gravity(grid)
    checked_normals.clear()

print(score)

# print()
# for r in range(N):
#     for c in range(N):
#         print(grid[r][c] if grid[r][c] != '' else ' ', end=" ")

#     print()
