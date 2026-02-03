from itertools import permutations

def solve_cryptarithmetic(puzzle):
    letters = list(set(puzzle.replace(" ", "").replace("=", "")))
    if len(letters) > 10:
        return None, 0
    left, right = puzzle.split('=')
    left_terms = [w.strip() for w in left.split('+')]
    right = right.strip()
    solutions = []
    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        if any(mapping[word[0]] == 0 for word in left_terms + [right]):
            continue
        left_sum = sum(int(''.join(str(mapping[c]) for c in word)) for word in left_terms)
        right_val = int(''.join(str(mapping[c]) for c in right))
        if left_sum == right_val:
            solutions.append(mapping)
    return solutions, len(solutions)

puzzle = "SEND + MORE = MONEY"
solutions, count = solve_cryptarithmetic(puzzle)
if solutions:
    print(f"Total solutions: {count}")
    for sol in solutions:
        print(sol)
else:
    print("No solution found.")
