from ortools.sat.python import cp_model

# Iniciamos el modelo y el solucionador
model = cp_model.CpModel()
solver = cp_model.CpSolver()

# 1. Variable
# Creamos una variable llamada "equipo" que representa el número de jugadores.
# La variable puede tener un valor entre 1 y 2000.
equipo = model.NewIntVar(1, 2000, 'jugadores')

# 2. Restricciones
# Establecemos tres restricciones en relación al número de jugadores:
# - El número de jugadores debe ser divisible por 5.
# - El número de jugadores debe ser divisible por 7.
# - El número de jugadores debe ser divisible por 11.
model.AddModuloEquality(0, equipo, 5)
model.AddModuloEquality(0, equipo, 7)
model.AddModuloEquality(0, equipo, 11)

# Encontrar la variable que favorece dichas restricciones
# Intentamos encontrar un valor para "equipo" que cumpla con las restricciones.
status = solver.Solve(model)

# Si se ha encontrado una solución, imprimimos los resultados

# Definimos una clase de callback para imprimir cada solución.
class PrintSolutions(cp_model.CpSolverSolutionCallback):
    def __init__(self, variable):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variable = variable

    def on_solution_callback(self):
        print(self.Value(self.__variable))

# Creamos una instancia de la clase de callback
solution_printer = PrintSolutions(equipo)

# Configuramos el solucionador para encontrar todas las soluciones posibles.
solver.parameters.enumerate_all_solutions = True

# Imprimimos todas las soluciones posibles.
print("Las posibles soluciones a nuestro problema son:")
status = solver.Solve(model, solution_printer)

# Encontrar el número mínimo de jugadores
# Minimizamos la variable "equipo" para encontrar el número mínimo de jugadores.
model.Minimize(equipo)
status = solver.Solve(model)

# Imprimimos el número mínimo de jugadores encontrado.
print('Número mínimo de jugadores:', solver.Value(equipo))

# Encontrar el número máximo de jugadores
# Maximizamos la variable "equipo" para encontrar el número máximo de jugadores.
model.Maximize(equipo)
status = solver.Solve(model)

# Imprimimos el número máximo de jugadores encontrado.
print('Número máximo de jugadores:', solver.Value(equipo))
