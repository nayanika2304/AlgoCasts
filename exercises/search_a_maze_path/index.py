# Using BFS - https://levelup.gitconnected.com/solve-a-maze-with-python-e9f0580979a1

"""
Approach 2 (Graph BFS or DFS)

We will imagine each cell as a vertex and each adjacent relationship as the edges connecting nodes.

Do we use DFS or BFS?

If we use BFS we know that the path that we find will be the shortest path because of how it searches (wide, going out layer by layer).

If we use DFS we can have the call stack remember the path making things easier to implement.

If we hit the end cell, then we will know that every call below in the call stack has a node apart of the answer path.

Since the problem just wants any path then we will use DFS since it is more straight-forward.


"""
from collections import defaultdict


class Solution:
    def findShortestDistance(self, maze, start, end):
        self.shortest=math.inf

        #set the default value of visited to be False
        self.visited=defaultdict(lambda: False)

        self.maze=maze
        self.rows=len(maze)
        self.cols=len(maze[0])
        self.depthFirstSearch(0,0,0)
        return self.shortest

    def depthFirstSearch(self, i, j, numStep):
        if i<0 or j<0 or i>=self.rows or j>=self.cols:
            return
        elif self.maze[i][j]=='o':
            return
        elif self.maze[i][j]=='g':
            self.shortest=min(self.shortest,numStep)
            return
        elif self.visited[(i,j)]:
            return

        self.visited[(i,j)] = True
        print("{} {}".format(i,j))
        self.depthFirstSearch(i-1,j,numStep+1)
        self.depthFirstSearch(i,j-1,numStep+1)
        self.depthFirstSearch(i,j+1,numStep+1)
        self.depthFirstSearch(i+1,j,numStep+1)

        return
