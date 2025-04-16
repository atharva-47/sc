# XOR with Backpropagation (Simple Version)
import numpy as np

# Sigmoid and its derivative
def sigmoid(x): return 1 / (1 + np.exp(-x))
def sigmoid_deriv(x): return x * (1 - x)

# XOR inputs and outputs
X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0], [1], [1], [0]])

# Weights and biases (random)
np.random.seed(0)
w1 = np.random.rand(2, 2)
w2 = np.random.rand(2, 1)
b1 = np.random.rand(1, 2)
b2 = np.random.rand(1, 1)

# Training loop
for epoch in range(10000):
    # Forward
    h = sigmoid(np.dot(X, w1) + b1)
    o = sigmoid(np.dot(h, w2) + b2)
    
    # Backward
    error = y - o
    d_o = error * sigmoid_deriv(o)
    d_h = d_o.dot(w2.T) * sigmoid_deriv(h)
    
    # Update weights and biases
    w2 += h.T.dot(d_o) * 0.1
    b2 += np.sum(d_o, axis=0) * 0.1
    w1 += X.T.dot(d_h) * 0.1
    b1 += np.sum(d_h, axis=0) * 0.1

# Final output
print("Final Output:")
print(o.round(3))
