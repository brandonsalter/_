import pandas as pd
import numpy as np

np.set_printoptions(precision=8, threshold=1000, edgeitems=3, linewidth=75, suppress=True, nanstr='nan', infstr='inf')

class LR:
    
    def __init__(self):
        pass
    
    def fit(self, df: pd.DataFrame, label: str):
        # Create coefficient matrix and dependent variable vector
        b = df[label].to_numpy()
        if df.iloc[:,0].sum() != len(df): # if there's no intercept column
            df.insert(loc = 0, column = 'x0', value = np.ones(len(df)))
        A = df.drop(label, axis=1).to_numpy()
        # Solve A_T_A x = A_T b for x
        A_T = np.transpose(A)
        A_T_A = np.matmul(A_T, A)
        A_T_b = np.matmul(A_T, b)
        x = np.linalg.solve(A_T_A, A_T_b)
        # Solve for p and compute sse
        p = np.matmul(A, x)
        e = b-p
        train_sse = (np.linalg.norm(e))**2.
        # Return intercept, coefficients, and sse
        intercept = x[0]
        coefficients = x[1:]
        return intercept, coefficients, train_sse