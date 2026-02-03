class ConstraintSatisfactionProblem:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def is_consistent(self, var, val, assignment):
        return all(constraint(var, val, assignment) for constraint in self.constraints.get(var, []))

    def backtrack(self, assignment={}):
        if len(assignment) == len(self.variables):
            return assignment
        var = next(v for v in self.variables if v not in assignment)
        for val in self.domains[var]:
            if self.is_consistent(var, val, assignment):
                assignment[var] = val
                result = self.backtrack(assignment)
                if result:
                    return result
                assignment.pop(var)
        return None

variables = ['A', 'B', 'C']
domains = {v: [1, 2, 3] for v in variables}
constraints = {
    'A': [lambda v, val, ass: 'B' not in ass or ass['B'] != val],
    'B': [lambda v, val, ass: 'A' not in ass or ass['A'] != val],
    'C': [
        lambda v, val, ass: 'A' not in ass or ass['A'] != val,
        lambda v, val, ass: 'B' not in ass or ass['B'] != val
    ]
}

csp = ConstraintSatisfactionProblem(variables, domains, constraints)
solution = csp.backtrack()
if solution:
    print("Solution found:", solution)
else:
    print("No solution found.")
