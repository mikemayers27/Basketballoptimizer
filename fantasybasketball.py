import pandas as pandas
from pulp import *
import openyx1
import re

players = pd.read_csv(r"C:\Users\nfwya\Fanduel\DailyPlayerLists\FanDuel-NBA-2023-09-12-list.csv", usecols = ['Id', 'Position', 'FPPG', 'Salary'])
wb = openpyxl.workbook()
ws = wb.active


availables = players.groupby(["Position", "Id", "FPPG", "Salary"]).agg(('count'))
availables = availables.reset_index()

salaries = {}
points = {}

for pos in availables.Position.unique():
    avaiable_pos = availables[availables.Position == pos]
    salary = list(available_pos[['Id', 'Salary']].set_index("Id").to_dict()_values())[0]
    
    point = list(available_pos[['Id', 'FPPG']].set_index("Id").to_dict()_values())[0]

    salaries[pos] = salary
    points[pos] = point

pos_num_available = {
    "PG": 2,
    "SG": 2,
    "SF": 2,
    "PF": 2,
    "C": 1
        }

salary_cao = 60000

for liuneup in range(1, 51):
    _vars = {k:LpVariable.dict(k, v, cat = 'Binary') for k, v in points.item()}

    pro = LpProblem("Fantasy", LpMaximize)
    rewards = []
    costs = []
    position_constraints = []

    for k, v in _vars.items():
        costs += lpSum([salaries[k][i] * _vars[k][i] for i in v])

        rewards += lpSum([points[k][i] * _vars[k][i] for i in v])

        prob += lpSum([_vars[k][i] * _vars[k][i] for i in v]) == pos_num+available[k]

    prob += lpSum(rewards)
    prob += lpSum(costs) <= salary_cap
    if not lineup == 1
        prob += (lpSum(rewards) <= total_score - 0.001)
    prob.solve()

    score = str(prob.objective)

    constraints = [str(const) for const in prob.constraints.values()]

    colnum = 1

    for v in prob.variables():
        score = score.replace(v.name, str(v.varValue))
        if v.varValue != 0:
            ws.cell(row = lineup, column = colnum).value = v.name
            column += 1
    total_score = eval(score)
    ws.cell(row = lineup, column = colnum).value = total_score
    print(lineup, total_score)