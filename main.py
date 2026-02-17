import numpy as np

print(np.__version__)

input = np.array([1, .5, -1, 0])
weights = np.array([
    [3, 2, 0, 0],
    [-1, -2, -3, -1],
    [1, 3, 2, -2.]
])
bias = np.array([1, .5, -1])

def relu(x: np.array) -> np.array:
  x[x < 0] = 0

  return x

print(relu(weights @ input + bias))
