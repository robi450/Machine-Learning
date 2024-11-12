import numpy as np
import matplotlib.pyplot as plt

# Generate random data points
np.random.seed(0) # For reproducibility
x = np.random.rand(100, 1) # 100 random x values
y = 2 * x + 1 + np.random.randn(100, 1) * 0.1 # Linear relationship with some noise

#Visualize the data
plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Generated Data')
plt.show()

# Initialize parameters
m = np.random.rand(1) # Random initial value for slope
b = np.random.rand(1) # Random initial value for intercept
learning_rate = 0.01 # Learning rate

# Define the cost function (Mean Squared Error)

def compute_cost(X, y, m, b):
    N = len(y)
    predictions = m * X + b
    cost = (1/N) * np.sum((predictions - y) ** 2)
    return cost

# Gradient Descent function 
# Write a function to update m and b using gradient descent:     

# Gradient Descent function
def gradient_descent(X, y, m, b, learning_rate, iterations):
    N = len(y)
    cost_history = []

    for i in range(iterations):
        # Calculate the gradients
        predictions = m * X + b
        m_gradient = -(2/N) * np.sum(X * (y - predictions))
        b_gradient = -(2/N) * np.sum(y - predictions)

        # Update parameters
        m -= learning_rate * m_gradient
        b -= learning_rate * b_gradient

        # Calculate and store the cost
        cost = compute_cost(X, y, m, b)
        cost_history.append(cost)

        # Print cost every 100 iterations for monitoring
        if i % 100 == 0:
            print(f"Iteration {i}: Cost {cost}")

    return m, b, cost_history

# Train the model
iterations = 1000  # Number of iterations for gradient descent
m, b, cost_history = gradient_descent(X, y, m, b, learning_rate, iterations)

print(f"Final parameters: m = {m}, b = {b}")

# Plot the data points and the regression line
plt.scatter(X, y)
plt.plot(X, m * X + b, color='red')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression Fit')
plt.show()

# Plot cost history to see how the cost decreases
plt.plot(range(iterations), cost_history)
plt.xlabel('Iterations')
plt.ylabel('Cost')
plt.title('Cost Reduction Over Time')
plt.show()


