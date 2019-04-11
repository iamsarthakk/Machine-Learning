import tensorflow as tf
import cv2
import PongGameimport numpy as np
import random
from collections import deque


ACTIONS = 3
GAMMA = 0.99 #LEARNING RATE
INITIAL_EPSILON = 1.0
FINAL_EPSILON = 0.05

#how many frames to anneal epsilon
EXPLORE = 500000
OBSERVE = 50000
REPLAY_MEMORY = 50000

BATCH = 100

def createGraph():
    #first convolutional layer and bias vector
    W_conv1 = tf.Variable(tf.zeroes([8, 8, 4, 32]))
    b_conv1 = tf.Varaiable(tf.zeroes[32])

    #second
    W_conv2 = tf.Variable(tf.zeroes[4, 4, 32, 64])
    b_conv2 = tf.Variable(tf.zeroes[64])

    #third
    W_conv2 = tf.Variable(tf.zeroes[3, 3, 64, 64])
    b_conv2 = tf.Variable(tf.zeroes[64])

    #forth
    W_fc4 = tf.Variable(tf.zeroes[784, ACTIONS])
    b_fc4 = tf.Variable(tf.zeroes[784])

    #Last layer
    W_fc5 = tf.Variable(tf.zeroes[784, ACTIONS])
    b_fc5 = tf.Variable(tf.zeroes[[ACTIONS]])

    s = tf.placeholder("float",[None, 84, 84, 84])

    #compute RELU activation function
    #on 2D convolutions
    #given 4D inputs and flte tensors

    conv1 = tf.nn.relu(tf.nn.conv2d(s, W_conv1, strides[1, 4, 4, 1] padding = "VALID") + b_conv1)
    conv2 = tf.nn.relu(tf.nn.conv2d(s, W_conv1, strides[1, 4, 4, 1] padding = "VALID") + b_conv1)
    conv3 = tf.nn.relu(tf.nn.conv2d(s, W_conv1, strides[1, 4, 4, 1] padding = "VALID") + b_conv1)

    conv3_flat = tf.reshape(conv3, [-1, 3136])
    fc4 = tf.nn.relu(tf.matmul(conv3_flat, w_fc4 + b_fc4))
    fc5 = tf.matmul(fc5,W_fc5) + b_fc5

    return s, fc5

def main():
    sess = tf.InteractiveSession()
    imp, ouy = CreateGraph()
    trainGraph(inp, out, sess)

if __name__ == '__main__':
    main()
