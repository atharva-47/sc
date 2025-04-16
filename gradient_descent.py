
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(0)
input_x = 5 * np.random.rand(100, 1)
actual_y = 2 + 3 * input_x + np.random.randn(100, 1)


input_x = input_x.flatten()
actual_y = actual_y.flatten()


def predict(inputs, weight, bias):
    return weight * inputs + bias

def gradient_descent(inputs, targets, learning_rate=0.01, epochs=100):
    weight = 0
    bias = 0
    n = len(inputs)
    loss_history = []

    for epoch in range(epochs):
        predicted = predict(inputs, weight, bias)
        error = predicted - targets
        loss = (1/n) * np.sum(error ** 2)
        loss_history.append(loss)

        d_weight = (2/n) * np.sum(error * inputs)
        d_bias = (2/n) * np.sum(error)

        weight -= learning_rate * d_weight
        bias -= learning_rate * d_bias

        if epoch % 49 == 0 :
            print(f"Epoch {epoch+1}: weight = {weight:.4f}, bias = {bias:.4f}, loss = {loss:.4f}")

    return weight, bias, loss_history


print("\n--- Training with 50 Epochs ---")
weight_50, bias_50, _ = gradient_descent(input_x, actual_y, epochs=50)

print("\n--- Training with 100 Epochs ---")
weight_100, bias_100, _ = gradient_descent(input_x, actual_y, epochs=100)

print("\n--- Training with 500 Epochs ---")

weight_500, bias_500, _ = gradient_descent(input_x, actual_y, epochs=500)


plt.scatter(input_x, actual_y, color='blue', label='Training Data')
plt.plot(input_x, predict(input_x, weight_50, bias_50), color='orange', label='Line (50 Epochs)')
plt.plot(input_x, predict(input_x, weight_100, bias_100), color='green', label='Line (100 Epochs)')
plt.plot(input_x, predict(input_x, weight_500, bias_500), color='cyan', label='Line (500 Epochs)')
plt.title('Linear Regression using Gradient Descent')
plt.xlabel('Input (x)')
plt.ylabel('Output (y)')
plt.legend()
plt.grid(True)
plt.show()
