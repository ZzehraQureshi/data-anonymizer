import numpy as np

def apply_differential_privacy(column, epsilon):
    """
    Adds Laplace noise to the numerical column to ensure differential privacy.
    """
    sensitivity = max(column) - min(column)
    noise = np.random.laplace(loc=0.0, scale=sensitivity/epsilon, size=len(column))
    return column + noise
