from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([
    ('Ranking', 'Win'),
    ('Serve',   'Win'),
    ('BreakPts','Win'),
    ('Errors',  'Win')
])

cpd_ranking = TabularCPD('Ranking', 2, [[0.5], [0.5]])
cpd_serve   = TabularCPD('Serve',   2, [[0.6], [0.4]])
cpd_bp      = TabularCPD('BreakPts',2, [[0.5], [0.5]])
cpd_errors  = TabularCPD('Errors',  2, [[0.5], [0.5]])

cpd_win = TabularCPD(
    variable='Win',
    variable_card=2,
    values=[
        [0.95, 0.80, 0.75, 0.60, 0.70, 0.55, 0.50, 0.35,
         0.65, 0.50, 0.45, 0.30, 0.40, 0.25, 0.20, 0.05],
        [0.05, 0.20, 0.25, 0.40, 0.30, 0.45, 0.50, 0.65,
         0.35, 0.50, 0.55, 0.70, 0.60, 0.75, 0.80, 0.95],
    ],
    evidence=['Ranking', 'Serve', 'BreakPts', 'Errors'],
    evidence_card=[2, 2, 2, 2]
)

model.add_cpds(cpd_ranking, cpd_serve, cpd_bp, cpd_errors, cpd_win)
print("Model valid:", model.check_model())

infer = VariableElimination(model)

print("\nScenario 1: Favored, good serve, good break pts, few errors")
print(infer.query(['Win'], evidence={'Ranking':0, 'Serve':0, 'BreakPts':0, 'Errors':0}))

print("\nScenario 2: Underdog, poor serve, poor break pts, many errors")
print(infer.query(['Win'], evidence={'Ranking':1, 'Serve':1, 'BreakPts':1, 'Errors':1}))

print("\nScenario 3: Favored player, but many errors")
print(infer.query(['Win'], evidence={'Ranking':0, 'Errors':1}))
