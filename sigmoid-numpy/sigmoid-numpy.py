import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    y = np.asarray(x, dtype = float)
    sig = 1/(1 + np.exp(-y))
    return sig# Write code here
    pass