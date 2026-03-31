import heapq

goal = [[1,2,3],[4,5,6],[7,8,0]]

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def heuristic(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                x = (val - 1) // 3
                y = (val - 1) % 3
                dist += abs(x - i) + abs(y - j)
    return dist

def to_tuple(state):
    return tuple(tuple(row) for row in state)

def get_neighbors(state):
    x, y = find_zero(state)
    moves = [(1,0),(-1,0),(0,1),(0,-1)]
    neighbors = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def solve(start):
    pq = []
    heapq.heappush(pq, (heuristic(start), 0, start, []))
    visited = set()
    while pq:
        f, g, state, path = heapq.heappop(pq)
        if state == goal:
            return path + [state]
        t = to_tuple(state)
        if t in visited:
            continue
        visited.add(t)
        for neighbor in get_neighbors(state):
            heapq.heappush(pq, (g + 1 + heuristic(neighbor), g + 1, neighbor, path + [state]))
    return None

start = [[1,2,3],[4,0,6],[7,5,8]]
solution = solve(start)

for step in solution:
    for row in step:
        print(row)
    print()
