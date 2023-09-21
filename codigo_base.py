from ortools.sat.python import cp_model

# Iniciamos el modelo y el solucionador
model = cp_model.CpModel()
solver = cp_model.CpSolver()

# 1. Variable
army = model.NewIntVar(1, 2000, 'jugadores')

# 2. Restricciones

model.AddModuloEquality(0, army, 5)
model.AddModuloEquality(0, army, 7)
model.AddModuloEquality(0, army, 11)

# Encontrar la variable que favorece dichas restricciones
status = solver.Solve(model)

# If a solution has been found, print results
# Find the variable that satisfies these constraints
status = solver.Solve(model)

# If a solution has been found, print results
class PrintSolutions(cp_model.CpSolverSolutionCallback):
    """Callback to print every solution."""
    def __init__(self, variable):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variable = variable
    def on_solution_callback(self):
        print(self.Value(self.__variable))

solution_printer = PrintSolutions(army)
solver.parameters.enumerate_all_solutions = True
print("Las posibles soluciones a nuestro problema son: ")
status = solver.Solve(model, solution_printer)

# número mínimo de jugadores
model.Minimize(army)

status = solver.Solve(model)

print('Número mínimo de jugadores: ', solver.Value(army))


# número máximo de jugadores
model.Maximize(army)

status = solver.Solve(model)

print('Número máximo de jugadores: ', solver.Value(army))