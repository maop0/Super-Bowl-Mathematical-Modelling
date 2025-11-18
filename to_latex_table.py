import numpy as np
import pandas as pd

def array_latex_table(mat):
    """
    input: np.array
    output:String
    """
    if len(mat.shape) != 2:
        raise ValueError("Input matrix must be 2-dimensional.")
    rows, cols = mat.shape
    latex_str = ""
    for i in range(rows):
        row_str = " & ".join([str(mat[i, j]) for j in range(cols)])
        latex_str += row_str + " \\"
    return latex_str

def csv_latex_table(file_path):
    """
    input: csv file path
    output:String
    """
    df = pd.read_csv(file_path)
    latex_str = df.to_latex(index=False, header=True)
    return latex_str

array_latex_table(np.array([[0.05  ,     0.04225352 ,0.07416564 ,0.02912621 ,0.02325581],
 [0.25   ,    0.21126761 ,0.17305315 ,0.34951456 ,0.34883721],
 [0.35 ,      0.63380282 ,0.51915946 ,0.46601942 ,0.34883721],
 [0.2   ,     0.07042254 ,0.12978986 ,0.11650485 ,0.20930233],
 [0.15   ,    0.04225352 ,0.10383189 ,0.03883495 ,0.06976744]]).T)