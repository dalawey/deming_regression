import pandas as pd
import numpy as np

def deming_regression(x_anon, y, x_noise, y_noise):
    """
    Perform Deming regression on the input data.

    Deming regression is an errors-in-variables model which tries to find
    the line of best fit for a two-dimensional dataset when there are errors
    in both the x and y variables.

    Parameters:
    -----------
    x_anon : array-like
        The x values of the dataset.
    y : array-like
        The y values of the dataset.
    x_noise : float
        The standard deviation of the noise in x.
    y_noise : float
        The standard deviation of the noise in y.

    Returns:
    --------
    tuple
        A tuple containing the intercept and slope of the regression line.

    """
    data = pd.DataFrame({'x': x_anon, 'y': y})
    x_mean = data['x'].mean()
    y_mean = data['y'].mean()
    cov = data.cov()
    s_xx = cov['x']['x']
    s_xy = cov['x']['y']
    s_yy = cov['y']['y']
    delta = (y_noise / x_noise) ** 2
    slope = (
        (s_yy - delta * s_xx + np.sqrt((s_yy - delta * s_xx) ** 2 + 4 * delta * s_xy ** 2))
        / (2 * s_xy)
    )
    intercept = y_mean - slope * x_mean
    return intercept, slope

