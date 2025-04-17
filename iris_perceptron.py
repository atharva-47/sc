import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.preprocessing import StandardScaler


iris = load_iris()
X = iris.data
y = iris.target


X = X[y != 0]        
y = y[y != 0]
y = y - 1           


scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


learning_rates = [0.000001, 0.01, 0.5, 1.0]
epoch_options = [10, 25, 50, 100]

# Set up plotting
plt.figure(figsize=(12, 8))

# Loop over combinations
for lr in learning_rates:
    for max_epoch in epoch_options:
        clf = Perceptron(eta0=lr, max_iter=1, warm_start=True, tol=None, random_state=42)
        train_accuracies = []
        
        for epoch in range(max_epoch):
            clf.fit(X_train, y_train)
            acc = clf.score(X_train, y_train)
            train_accuracies.append(acc)

        label = f"LR={lr}, Epochs={max_epoch}"
        plt.plot(range(1, max_epoch + 1), train_accuracies, label=label)

# Finalize plot
plt.title("Training Accuracy for Different Learning Rates and Iteration Counts")
plt.xlabel("Epoch")
plt.ylabel("Training Accuracy")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
