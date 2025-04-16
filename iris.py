# # Slip E - Simple Iris Classification using two features and graph

# import matplotlib.pyplot as plt
# from sklearn.datasets import load_iris

# # Load dataset
# iris = load_iris()
# X = iris.data  # Features
# y = iris.target  # Labels
# target_names = iris.target_names

# # We'll use only the first two features for simplicity: sepal length and sepal width
# x_feature = X[:, 0]  # sepal length
# y_feature = X[:, 1]  # sepal width

# # Plot data points with different colors for each class
# colors = ['red', 'green', 'blue']
# for i in range(3):
#     plt.scatter(
#         x_feature[y == i],
#         y_feature[y == i],
#         color=colors[i],
#         label=target_names[i]
#     )

# # Labels and title
# plt.xlabel("Sepal Length (cm)")
# plt.ylabel("Sepal Width (cm)")
# plt.title("Iris Dataset - Simple Classification Graph")
# plt.legend()
# plt.grid(True)
# plt.show()


# Slip XX - Simple Iris classification with graph

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

# Use only two features for easy plotting
X = df[['sepal length (cm)', 'sepal width (cm)']]
y = df['target']

# Train a simple classifier
model = LogisticRegression()
model.fit(X, y)

# Plot the data points
plt.figure(figsize=(7, 5))
colors = ['red', 'green', 'blue']
for i in range(3):
    subset = df[df['target'] == i]
    plt.scatter(subset['sepal length (cm)'], subset['sepal width (cm)'],
                color=colors[i], label=iris.target_names[i])

plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('Iris Dataset - Simple Plot by Class')
plt.legend()

plt.show()

