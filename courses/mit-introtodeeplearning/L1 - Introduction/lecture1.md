Detailed Summary for [MIT Introduction to Deep Learning | 6.S191](https://www.youtube.com/watch?v=QDX-1M5Nj7s&list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI&index=2) by [Monica](https://monica.im)

[00:09](https://www.youtube.com/watch?v=QDX-1M5Nj7s&list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI&index=2&t=9.12) Alexander Amini introduces MIT's Introduction to Deep Learning course, which covers the foundations of deep learning and artificial intelligence and provides hands-on experience with software labs.
- The course covers a lot of material in just one week.
- Deep learning has had a huge resurgence in the past decade with many incredible successes and has solved problems that were previously thought to be unsolvable.
- The past year, in particular, has been the year of generative deep learning, using deep learning to generate brand new types of data that have never been seen before.
- The introductory video for the course exemplifies the idea of generative deep learning.

[07:18](https://www.youtube.com/watch?v=QDX-1M5Nj7s&list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI&index=2&t=438.18) This class teaches how to build and teach computers to learn tasks from raw data using neural networks.
- The class is split between technical lectures and software labs.
- The technical lectures cover the foundations of deep learning.
- The software labs provide hands-on experience implementing the ideas covered in the technical part of the class.
- The course concludes with guest lectures from both academia and industry leading the state of AI and deep learning, as well as a project competition with prizes.

[14:50](https://www.youtube.com/watch?v=QDX-1M5Nj7s&list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI&index=2&t=873.3) The fundamental building block of every single neural network is a ***<span style="color: red;">Perceptron</span>***
, which takes inputs, multiplies them by corresponding weights, adds a bias term, passes through a non-linear activation function, and produces the final output.
- A perceptron is a single neuron in a neural network that takes M different inputs.
- Each input is multiplied by a corresponding weight and added together with a bias term.
- The result is passed through a non-linear activation function to produce the final output.

[21:53](https://www.youtube.com/watch?v=QDX-1M5Nj7s&list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI&index=2&t=1313.52) The perceptron's output is determined by which side of the space it lives on, and the sigmoid function controls movement to one side or the other.
- The output of the perceptron is positive if it lives on one side of the plane.
- The thresholding function lives at the decision boundary.
- The sigmoid function controls movement to one side or the other depending on which side of the space the perceptron lives on.
- Drawing plots like the one shown is not feasible for data with thousands or millions of dimensions.

[29:08](https://www.youtube.com/watch?v=QDX-1M5Nj7s&list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI&index=2&t=1748.64) <span style="color: red;">Deep Neural Networks</span> can be created by stacking multiple layers, with the last layer being the output layer for final prediction.
- A deep neural network is created by stacking layers to create hierarchical models.
- The final prediction is made in the output layer.
- A simple neural network with two inputs can be trained to solve a real problem of predicting whether a student will pass a class.
- The neural network can be trained using data from past years and plotted on a two-dimensional feature space.

[36:26](https://www.youtube.com/watch?v=QDX-1M5Nj7s&list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI&index=2&t=2186.46) To find the optimal weights for a neural network, start at a random point in the weight space, evaluate the neural network, compute the gradient of the loss, negate the gradient and take a step in the opposite direction to decrease the loss, and repeat the process.
- Loss function J of w is a function of weights that computes the error of the neural network for any instantiation of the weights.
- The loss can be visualized in a two-dimensional space for a simple neural network with two weights.
- The optimal weights that would train this neural network are the ones that give the smallest loss possible, which is the lowest point on the landscape.
- The gradient of the loss tells us the direction of the highest point, and we take a step in the opposite direction to decrease the loss.

[43:40](https://www.youtube.com/watch?v=QDX-1M5Nj7s&list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI&index=2&t=2620.98) The learning rate in gradient descent can be challenging to set for neural networks.
- Learning rate determines how big of a step to take in the direction of the gradient during backpropagation.
- Setting the learning rate too low leads to slow convergence and getting stuck in local minimum.
- Setting the learning rate too high can cause overshooting and divergence from the solution.
- There is a happy medium between setting it too small and too large to converge on the solutions that matter.

[50:58](https://www.youtube.com/watch?v=QDX-1M5Nj7s&list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI&index=2&t=3058.56) Averaging over a batch allows for a higher learning rate and parallelization, while overfitting is a challenge when extracting patterns from <span style="color: red;">training</span> data.
- Averaging over a batch allows for a higher learning rate and parallelization.
- Overfitting is a challenge when extracting patterns from training data.
- The goal is to build models that can learn representations from training data that can still generalize to new test data.
