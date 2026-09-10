"""Various math functions
"""

def get_array_mean(V):
    """Compute the arithmetic mean of an array. Expects a non-empty array.

    Parameters
    ----------
    V : list of int
        Non-empty array containing numbers whose mean is desired.

    Returns
    -------
    m
        Arithmetic mean of the values in V
    
    """
    m = sum(V)/len(V)
    return m
