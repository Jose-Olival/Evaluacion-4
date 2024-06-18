import pandas as pd
from scipy.optimize import linear_sum_assignment

def leer_preferencias(archivo_csv):
    return pd.read_csv(archivo_csv, index_col=0)

def asignacion_optima(df):
    cost_matrix = -df.values
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    return row_ind, col_ind

def main():
    df = leer_preferencias('preferencias.csv')
    
    row_ind, col_ind = asignacion_optima(df)
    
    total_preferencias = -df.values[row_ind, col_ind].sum()
    
    print("Asignación óptima de profesores a cursos:")
    for i in range(len(row_ind)):
        print(f"El profesor {df.columns[col_ind[i]]} dictará el curso {df.index[row_ind[i]]}")
    print(f"Total de las preferencias maximizadas: {total_preferencias}")

if name == "main":
    main()



