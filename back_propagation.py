import numpy as np

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Input data
X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float) / 9
y = np.array(([92], [86], [89]), dtype=float) / 100

# Neural network parameters
input_neurons, hidden_neurons, output_neurons = 2, 3, 1
epoch, lr = 7000, 0.1

# Initialize weights and biases
wh = np.random.uniform(size=(input_neurons, hidden_neurons))
wout = np.random.uniform(size=(hidden_neurons, output_neurons))
bh = np.random.uniform(size=(1, hidden_neurons))
bout = np.random.uniform(size=(1, output_neurons))

# Training
for i in range(epoch):
    # Forward propagation
    hinp = np.dot(X, wh) + bh
    hlayer_act = sigmoid(hinp)
    outinp = np.dot(hlayer_act, wout) + bout
    output = sigmoid(outinp)

    # Backpropagation
    EO = y - output
    d_output = EO * output * (1 - output)
    EH = d_output.dot(wout.T) * hlayer_act * (1 - hlayer_act)

    # Update weights and biases
    wout += hlayer_act.T.dot(d_output) * lr
    wh += X.T.dot(EH) * lr

# Print results
print(f"Input:\n{X}")
print(f"Actual Output:\n{y}")
print(f"Predicted Output:\n{output}")