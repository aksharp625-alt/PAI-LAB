class CSP:
    def __init__(self, variables, domains, neighbors, constraints):
        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
        self.constraints = constraints

    def is_consistent(self, var, value, assignment):
        for neighbor in self.neighbors[var]:
            if neighbor in assignment:
                if not self.constraints(var, value, neighbor, assignment[neighbor]):
                    return False
        return True

    def select_unassigned_variable(self, assignment):
        for var in self.variables:
            if var not in assignment:
                return var
        return None

    def backtrack(self, assignment):
        if len(assignment) == len(self.variables):
            return assignment
        var = self.select_unassigned_variable(assignment)
        for value in self.domains[var]:
            if self.is_consistent(var, value, assignment):
                assignment[var] = value
                result = self.backtrack(assignment)
                if result:
                    return result
                del assignment[var]
        return None

def different(x, vx, y, vy):
    return vx != vy

variables = ["A", "B", "C"]
domains = {
    "A": [1, 2, 3],
    "B": [1, 2, 3],
    "C": [1, 2, 3]
}
neighbors = {
    "A": ["B", "C"],
    "B": ["A", "C"],
    "C": ["A", "B"]
}

csp = CSP(variables, domains, neighbors, different)
solution = csp.backtrack({})

print(solution)
