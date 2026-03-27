import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    y = np.asarray(x, dtype = float)
    t = (np.exp(y)-np.exp(-y))/(np.exp(y)+np.exp(-y))
    return t
    pass