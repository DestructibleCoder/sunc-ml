import numpy as np
from decor import functime

@functime
def prod_non_zero_diag(x):
    diag = x.diagonal()
    return np.prod(diag[diag != 0])

@functime
def are_multisets_equal(x, y):
    return np.array_equal(np.sort(x), np.sort(y))

@functime
def max_after_zero(x):
    mask = (x[:-1] == 0)
    return x[1:][mask].max()

@functime
def convert_image(img, coefs):
    return np.dot(img, coefs)

@functime
def run_length_encoding(x):
    if x.size == 0:
        return np.array([]), np.array([])
        
    change_indices = np.nonzero(x[1:] != x[:-1])[0] + 1
    run_starts = np.r_[0, change_indices]
    run_ends = np.r_[change_indices, x.size]
    
    elements = x[run_starts]
    counters = run_ends - run_starts
    
    return elements, counters

@functime
def pairwise_distance(x, y):
    diff = x[:, np.newaxis, :] - y[np.newaxis, :, :]
    return np.sqrt(np.sum(diff ** 2, axis=-1))
    
