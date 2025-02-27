import numpy as np

X = np.random.randn(4, 5)
print(X)
X.flatten()
print(X)
print(X > 0)
print(X[X > 0])

"""
[[-0.39433298 -0.41114775  0.15553956 -1.70161504 -1.52779906]
 [-0.23503521  1.47302734 -0.33928232 -0.79443819 -0.05557626]
 [-0.61837364 -0.30563972 -3.42271547 -1.30967393  0.69954827]
 [ 1.53520279  0.22760322  0.67797615  0.1298327   0.26368056]]
[[-0.39433298 -0.41114775  0.15553956 -1.70161504 -1.52779906]
 [-0.23503521  1.47302734 -0.33928232 -0.79443819 -0.05557626]
 [-0.61837364 -0.30563972 -3.42271547 -1.30967393  0.69954827]
 [ 1.53520279  0.22760322  0.67797615  0.1298327   0.26368056]]
[[False False  True False False]
 [False  True False False False]
 [False False False False  True]
 [ True  True  True  True  True]]
[0.15553956 1.47302734 0.69954827 1.53520279 0.22760322 0.67797615
 0.1298327  0.26368056]
"""
