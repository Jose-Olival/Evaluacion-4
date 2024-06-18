import csv
import numpy as np
from scipy.optimize import linear_sum_assignment

def leer_preferencias(archivo_csv):
    with open(archivo_csv, newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)[1:]  # Omitir la primera celda vacía/identificador
        data = list(reader)
        indices = [row[0] for row in data]
        values = [row[1:] for row in data]
    return np.array(values, dtype=float), indices, headers

def asignacion_optima(values):
    cost_matrix = -values
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    return row_ind, col_ind

def main():
    values, indices, headers = leer_preferencias('preferencias.csv')
    
    row_ind, col_ind = asignacion_optima(values)
    
    total_preferencias = -values[row_ind, col_ind].sum()
    
    print("Asignación óptima de profesores a cursos:")
    for i in range(len(row_ind)):
        print(f"El profesor {headers[col_ind[i]]} dictará el curso {indices[row_ind[i]]}")
    print(f"Total de las preferencias maximizadas: {total_preferencias}")

if __name__ == "__main__":
    main()


