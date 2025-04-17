from sklearn.datasets import fetch_openml
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import numpy as np

# Load MNIST
X, y = fetch_openml('mnist_784', version=1, return_X_y=True)

# Filter only digits 0 and 1
mask = (y == '0') | (y == '9')
X_binary = X[mask]
y_binary = y[mask].astype(int)

# Normalize pixel values
X_binary = X_binary / 255.0

# Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(X_binary, y_binary, test_size=0.2, random_state=42)

# Try different learning rates
learning_rates = [0.0001, 0.01, 0.5, 1.0]

for lr in learning_rates:
    model = Perceptron(max_iter=1000, eta0=lr, tol=1e-3)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Learning Rate: {lr:.4f} -> Accuracy: {acc:.4f}")

