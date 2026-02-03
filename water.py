from collections import deque

def water_jug(a, b, target):
    visited = set()
    q = deque()
    q.append((0, 0, []))

    while q:
        x, y, path = q.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        path = path + [(x, y)]

        if x == target or y == target:
            for state in path:
                print(state)
            return

        next_states = [
            (a, y),
            (x, b),
            (0, y),
            (x, 0),
            (x - min(x, b - y), y + min(x, b - y)),
            (x + min(y, a - x), y - min(y, a - x))
        ]

        for state in next_states:
            q.append((state[0], state[1], path))

    print("Solution not possible")

Jug1 = int(input("Enter capacity of Jug1: "))
Jug2 = int(input("Enter capacity of Jug2: "))
target = int(input("Enter target: "))
water_jug(Jug1, Jug2, target)
