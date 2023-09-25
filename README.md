# INTRODUCCION-A-LA-PROGRAMACI-N-CON-RESTRICCIONES

Miembros del grupo: Germán Llorente y Carlos Puigserver

El link al repositorio es el siguiente: https://github.com/Germiprogramer/INTRODUCCION-A-LA-PROGRAMACI-N-CON-RESTRICCIONES.git

La información solicitada acerca del tema está expuesta en el latex, mientras que todo lo relacionado al problema propuesto y su código están en los archivos de código y en el readme.

# Problema de Satisfacibilidad propuesto

Una asociación de fútbol celebra el 50 aniversario de su fundación. Para ello, se quiere organizar un torneo masivo en el que se combinen tres modalidades distintas del deporte: fútbol sala (5 jugadores por equipo), fútbol 7 (7 jugadores por equipo) y la modalidad tradicional (11 jugadores por equipo). Debido a la popularidad del evento, los organizadores han decidido restringir la cantidad máxima de participantes a 2000. El objetivo del problema es encontrar las distintas cantidades de personas que podrían participar en el evento, destacando el máximo y el mínimo número de individuos.

El código utiliza la biblioteca ortools para resolver este problema de optimización. Aquí está la explicación del código en relación al problema:

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

En resumen, el código encuentra el número de jugadores que cumplen con las restricciones del torneo y también determina el número mínimo y máximo de jugadores que pueden participar en el evento.
