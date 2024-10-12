# Redes Neurais - Apresentação
1. Introdução a Redes Neurais Aplicadas e Robótica - Introdução e ferramentas
2. Modelos Lineares, Regressão Logística, Perceptron e Multilayer Perceptron
3. Redes Convolucionais (CNN) MLP
4. Redes Convolucionais (CNN) e MLOps
5. Autoencoders e GANs (Redes Generativas)
6. Redes Neurais Recorrentes
7. Transformers

## Aprendizagem Profunda (Deep Learning)
1. Introduction
2. Preliminaries
3. Linear Neural Networks
4. Multilayer Perceptron
5. Deep Learning Computation
6. Convolutional Neural Networks
7. Modern Convolutional Neural Networks
8. Recurrent Neural Networks
9. Modern Recurrent Neural Networks
10. Attention Mechanisms
11. Optimization Algorithms
12. Computational Performance
13. Computer Vision
14. Natural Language Processing

### Fontes (Livros)
- [Dive into Deep Learning](https://d2l.ai/)
- Neural Networks and Deep Learning
- [Deep Learning](https://www.deeplearningbook.org/)

> To proceed on the basis of the conjecture that every aspect of learning or any other feature of intelligence can in principle be so precisely described that a machine can be made to simulate it.

## Paradigma
### Traditional Programming:
Data (INPUT) + Program -> Output

Input + Rules -> Answers

### Machine Learning:
Data (INPUT) + Output -> Program

Input + Answers -> Rules

## Neural Network - Perceptron
The perceptron is a simple model of a biological neuron. It receives input signals through its dendrites, which are then combined into a single signal and sent along its axon. In the artificial model, the input signals are multiplied by weights, which are then summed up. The sum is then passed through an activation function to produce the output.

### UAT - Universal Approximation Theorem
A feedforward neural network with a single layer containing a finite number of neurons can approximate continuous functions on compact subsets of R^n, under mild assumptions on the activation function.

## Neural Network - Backpropagation
Backpropagation is a method used in artificial neural networks to calculate a gradient that is needed in the calculation of the weights to be used in the network. It is commonly used to train deep neural networks, a term used for neural networks with more than one hidden layer.