# Rotting Oranges
# In a given grid, each cell can have one of three values:

# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.


# Example 1:
# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

# Example 3:
# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

# Note:

# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] is only 0, 1, or 2.

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))    
        # Check for fresh adjacent oranges. Turn them into rotten oranges and add them to queue
        def processAdjacentOranges(pos):
            if pos[0] < 0 or pos[1] < 0 or pos[0] >= rows or pos[1] >= cols:
                return

            if grid[pos[0]][pos[1]] == 1:
                grid[pos[0]][pos[1]] = 2
                queue.append((pos[0], pos[1]))

        direct = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        count = 0
        while queue:
            # Process only the current queue length, and not the ones added later
            # One cycle here is one minute
            for _ in range(len(queue)):
                pos = queue[0]
                queue.pop(0)
                for i in range(4):
                    processAdjacentOranges((pos[0] + direct[i][0], pos[1] + direct[i][1]))
            if queue:
                count += 1
        # Return -1 if there are still fresh oranges left
        if any(1 in row for row in grid):
            return -1
        return count