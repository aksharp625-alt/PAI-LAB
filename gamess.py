def minimax(depth, index, isMax, scores, targetDepth):
    if depth == targetDepth:
        return scores[index]

    if isMax:
        return max(minimax(depth + 1, index * 2, False, scores, targetDepth),
                   minimax(depth + 1, index * 2 + 1, False, scores, targetDepth))
    else:
        return min(minimax(depth + 1, index * 2, True, scores, targetDepth),
                   minimax(depth + 1, index * 2 + 1, True, scores, targetDepth))

scores = [3, 5, 2, 9, 12, 5, 23, 23]
treeDepth = 3  

print("The optimal value is : ", minimax(0, 0, True, scores, treeDepth))
