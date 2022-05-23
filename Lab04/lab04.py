from Stack import Stack
def solveMaze(maze, startx, starty):
    count = 1
    pos = Stack()
    x = startx
    y = starty
    Row = len(maze)
    Col = len(maze[0])
    pos.push([x,y])
    while pos.size() > 0:
        cur_pos = pos.peek()
        pos.pop()
        x = cur_pos[0]
        y = cur_pos[1]
        if (x < 0) or (y < 0) or (x >= Row) or (y >= Col):
            continue
        if maze[x][y] == 'G':
            return True
        if maze[x][y] != ' ':
            continue

        maze[x][y] = count
        count += 1
        
        pos.push([x,y+1])
        pos.push([x+1,y])
        pos.push([x,y-1])
        pos.push([x-1,y])
    return False

def printMaze(maze):
	for row in range(len(maze)):
		for col in range(len(maze[0])):
			print("|{:<2}".format(maze[row][col]), sep='',end='')
		print("|")
	return
            
        
        