import numpy as np

def to_latex_table(mat):
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
        latex_str += row_str + " \\\\\n"
    return latex_str

