import numpy as np
from typing import List, Tuple, Optional
from numpy.typing import ArrayLike


def sigmoid(z: ArrayLike) -> ArrayLike:
    """Sigmoid function that takes in an array and returns the sigmoid
    of each element in the array. The sigmoid function is defined as
    1/(1 + exp(-z)). This function is used to convert the output of a
    neuron to a value between 0 and 1.

    Args:
        z (ArrayLike): Array of values to apply the sigmoid function to.

    Returns:
        ArrayLike: Array of values between 0 and 1.
    """
    return 1.0/(1.0 + np.exp(-z))


def sigmoid_prime(z: ArrayLike) -> ArrayLike:
    """Derivative of the sigmoid function. The derivative of the sigmoid
    function is defined as sigmoid(z) * (1 - sigmoid(z)). This function is
    used to calculate the gradient of the cost function with respect to
    the weights and biases.

    Args:
        z (ArrayLike): Array of values to apply the sigmoid prime function to.

    Returns:
        ArrayLike: Array of values between 0 and 1.
    """
    return sigmoid(z) * (1 - sigmoid(z))


class Network:

    def __init__(self, sizes: List[int]) -> None:
        """Initializes the network with random weights and biases
        for each layer.

        The list `sizes` contains the number of neurons in the
        respective layers of the network. For example, if the list
        was `[2, 3, 1]` then it would be a three-layer network, with the
        first layer containing 2 neurons, the second layer 3 neurons,
        and the third layer 1 neuron. The biases and weights for the
        network are initialized randomly, using a Gaussian
        distribution with mean 0, and variance 1. Note that the first
        layer is assumed to be an input layer, and by convention we
        won't set any biases for those neurons, since biases are only
        ever used in computing the outputs from later layers.

        So, for example, if we want to create a Network object with 2 neurons
        in the first layer, 3 neurons in the second layer, and 1 neuron in the
        final layer, we'd do this with the code:
        `net = Network([2, 3, 1])`

        Args:
            sizes (List[int]): List of integers where each integer
            represents the number of neurons in each layer.
        """
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]

    def feedfoward(self, a: ArrayLike) -> ArrayLike:
        """Feedfoward function that takes in an input array and returns
        the output of the network. This is done by applying the sigmoid
        function to the weighted sum of the inputs and biases for each
        layer.

        Args:
            a (ArrayLike): Input array to the network.

        Returns:
            ArrayLike: Output of the network.
        """
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a) + b)
        return a

    def cost_derivative(
        self,
        output_activations: ArrayLike,
        y: ArrayLike,
    ) -> ArrayLike:
        """Return the vector of partial derivatives \\ partial C_x /
        \\ partial a for the output activations.

        Args:
            output_activations (ArrayLike): Output of the network.
            y (ArrayLike): Expected output.

        Returns:
            ArrayLike: Vector of partial derivatives.
        """
        return output_activations - y

    def backprop(
        self,
        x: ArrayLike,
        y: ArrayLike,
    ) -> Tuple[List[ArrayLike], List[ArrayLike]]:
        """Backpropagation algorithm that takes in an input array `x` and
        the expected output array `y`. The function returns a tuple of
        lists containing the gradients for the biases and weights for
        each layer.

        `nabla_b` and
        `nabla_w` are layer-by-layer lists of numpy arrays, similar
        to `self.biases` and `self.weights`.

        Args:
            x (ArrayLike): Input array.
            y (ArrayLike): Expected output array.

        Returns:
            Tuple[ List[ArrayLike], List[ArrayLike] ]: Tuple containing the
            gradients for the biases and weights for each layer.
        """
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]

        activation = x
        activations = [x]
        zs = []

        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation) + b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)

        cd = self.cost_derivative(activations[-1], y)
        delta = cd * sigmoid_prime(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())

        for layer in range(2, self.num_layers):
            z = zs[-layer]
            sp = sigmoid_prime(z)
            delta = np.dot(self.weights[-1+1].transpose(), delta) * sp
            nabla_b[-layer] = delta
            nabla_w[-layer] = np.dot(delta, activations[-layer-1].transpose())
        return (nabla_b, nabla_w)

    def update_mini_batch(
        self,
        mini_batch: List[Tuple[ArrayLike, ArrayLike]],
        eta: float,
    ) -> None:
        """Update the network's weights and biases by applying gradient
        descent using backpropagation to a single mini batch. The `mini_batch`
        is a list of tuples `(x, y)` and `eta` is the learning rate. This
        function updates the weights and biases by applying gradient descent
        using backpropagation to a single mini batch.

        Args:
            mini_batch (List[Tuple[ArrayLike, ArrayLike]]): List of tuples
            where the first element is the input array and the second element
            is the output array.
            eta (float): Learning rate.
        """
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]

        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backprop(x, y)
            nabla_b = [nb + dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw + dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        self.weights = [w - (eta/len(mini_batch)) * nw
                        for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b - (eta/len(mini_batch)) * nb
                       for b, nb in zip(self.biases, nabla_b)]

    def evaluate(
        self,
        test_data: List[Tuple[ArrayLike, ArrayLike]],
    ) -> int:
        """Return the number of test inputs for which the neural network
        outputs the correct result. Note that the neural network's output
        is assumed to be the index of whichever neuron in the final layer
        has the highest activation.

        Args:
            test_data (List[Tuple]List[Tuple[ArrayLike, ArrayLike]]): List
            of tuples where the first element is the input array and the
            second element is the output array.

        Returns:
            int: Number of test inputs for which the neural network outputs
            the correct result.
        """
        test_results = [(np.argmax(self.feedfoward(x)), y)
                        for x, y in test_data]
        return sum(int(x == y) for x, y in test_results)

    def SGD(
        self,
        training_data: List[Tuple[ArrayLike, ArrayLike]],
        epochs: int,
        mini_batch_size: int,
        eta: float,
        test_data: Optional[List[Tuple[ArrayLike, ArrayLike]]] = None,
    ) -> None:
        """Stochastic Gradient Descent:
        Train the neural network using mini-batch stochastic
        gradient descent.  The "training_data" is a list of tuples
        "(x, y)" representing the training inputs and the desired
        outputs.  The other non-optional parameters are
        self-explanatory.  If "test_data" is provided then the
        network will be evaluated against the test data after each
        epoch, and partial progress printed out.  This is useful for
        tracking progress, but slows things down substantially."""
        if test_data:
            n_test = len(test_data)
        n = len(training_data)
        for j in range(epochs):
            np.random.shuffle(training_data)
            mini_batches = [training_data[k:k+mini_batch_size]
                            for k in range(0, n, mini_batch_size)]
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta)
            if test_data:
                print(f'Epoch {j}: {self.evaluate(test_data)}/{n_test}')
            else:
                print(f'Epoch {j} complete.')


if __name__ == "__main__":
    net = Network([2, 3, 1])
