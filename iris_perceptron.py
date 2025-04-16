# Slip Ref: Perceptron on IRIS - Versicolor vs Virginica with learning rate variations

from sklearn.datasets import load_iris
from sklearn.linear_model import Perceptron
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load harder binary classes: Versicolor (1) vs Virginica (2)
X, y = load_iris(return_X_y=True)
X = X[50:]  # Take last 100 samples (classes 1 and 2)
y = y[50:]
y = (y == 1).astype(int)  # Versicolor = 1, Virginica = 0

# Scale features
X = StandardScaler().fit_transform(X)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Train with different learning rates
learning_rates = [0.0001, 0.01, 0.5, 1.0]
epochs = 25
plt.figure(figsize=(10, 6))

for lr in learning_rates:
    model = Perceptron(eta0=lr, max_iter=1, warm_start=True, tol=None)
    acc_list = []
    for _ in range(epochs):
        model.fit(X_train, y_train)
        acc = model.score(X_test, y_test)
        acc_list.append(acc)
        print("Accuracy : ", acc)
    plt.plot(range(1, epochs + 1), acc_list, label=f'LR={lr}')

plt.title("Perceptron Accuracy vs Epochs (Versicolor vs Virginica)")
plt.xlabel("Epochs")
plt.ylabel("Test Accuracy")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

