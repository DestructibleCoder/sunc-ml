from decor import functime

@functime
def prod_non_zero_diag(x):
    prod = 1
    for i in range(min(len(x), len(x[0]))):
        prod *= x[i][i] if x[i][i] != 0 else 1

    return prod

@functime
def are_multisets_equal(x, y):
    if len(x) != len(y):
        return False
        
    sorted_x = sorted(x)
    sorted_y = sorted(y)

    for i, j in zip(sorted_x, sorted_y):
        if i != j:
            return False

    return True

@functime
def max_after_zero(x):
    max_element = float('-inf')
    for i in range(len(x)):
        if x[i] == 0 and i+1 < len(x):
            if x[i+1] > max_element:
                max_element = x[i+1]

    return max_element

@functime
def convert_image(img, coefs):
    height = len(img)
    width = len(img[0])
    num_channels = len(coefs)
    
    result = [[0.0 for _ in range(width)] for _ in range(height)]
    
    for i in range(height):
        for j in range(width):
            val = 0.0
            for k in range(num_channels):
                val += img[i][j][k] * coefs[k]
            result[i][j] = val
            
    return result

@functime
def run_length_encoding(x):
    if len(x) == 0:
        return [], []
        
    elements = [x[0]]
    counters = [1]
    
    for i in range(1, len(x)):
        if x[i] == x[i-1]:
            counters[-1] += 1
        else:
            elements.append(x[i])
            counters.append(1)
            
    return elements, counters

@functime
def pairwise_distance(x, y):
    distances = [[0.0 for _ in range(len(y))] for _ in range(len(x))]
    
    for i in range(len(x)):
        for j in range(len(y)):
            dist = 0.0
            for k in range(len(x[i])):
                dist += (x[i][k] - y[j][k]) ** 2
            distances[i][j] = dist ** 0.5
            
    return distances