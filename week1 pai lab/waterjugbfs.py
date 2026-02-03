from collections import deque
def water_jug_optimal(jug1,jug2,target):
    visited=set()
    q=deque()
    q.append((0,0,[(0,0)]))
    while q:
        x,y,path=q.popleft()
        if (x,y) in visited:
            continue
        visited.add((x,y))
        if x == target:
            print("Solution is found\n")
            print("Optimal steps (BFS):\n")
            for i, state in enumerate(path):
                print(f"Step {i}: {state}")
            print("\nTotal steps =", len(path)-1)
            return

        next_states = [
            (jug1,y),   
            (x,jug2),   
            (0,y),      
            (x,0),      
            (x-min(x,jug2-y),y+min(x,jug2-y)),  
            (x+min(y,jug1-x),y-min(y,jug1-x))   
        ]

        for nx, ny in next_states:
            if (nx,ny) not in visited:
                q.append((nx,ny,path+[(nx,ny)]))
    print("Solution is not found")
if __name__ == "__main__":
    j1 = int(input("Enter Jug1 capacity: "))
    j2 = int(input("Enter Jug2 capacity: "))
    target = int(input("Enter target: "))
    water_jug_optimal(j1,j2,target)



