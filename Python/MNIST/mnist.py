import numpy as np
import matplotlib.pyplot as plt
import pickle
from scipy.stats import truncnorm

image_size = 28 # width and length
no_of_different_labels = 10 #  i.e. 0, 1, 2, 3, ..., 9
image_pixels = image_size * image_size
train_data = np.loadtxt("mnist_train.csv", delimiter=",")
test_data = np.loadtxt("mnist_test.csv", delimiter=",")

#Map Image data between 0.01 to 0.99 (previously 0 to 255)
fac = 255  *0.99 + 0.01
train_imgs = np.asfarray(train_data[:, 1:]) / fac
test_imgs = np.asfarray(test_data[:, 1:]) / fac
train_labels = np.asfarray(train_data[:, :1])
test_labels = np.asfarray(test_data[:, :1])

lr = np.arange(no_of_different_labels)
# transform labels into one hot representation eg. one hot representation of 0: [1 0 0 0 0 0 0 0 0 0]
train_labels_one_hot = (lr==train_labels).astype(np.float)
test_labels_one_hot = (lr==test_labels).astype(np.float)
# we don't want zeroes and ones in the labels neither:
train_labels_one_hot[train_labels_one_hot==0] = 0.01
train_labels_one_hot[train_labels_one_hot==1] = 0.99
test_labels_one_hot[test_labels_one_hot==0] = 0.01
test_labels_one_hot[test_labels_one_hot==1] = 0.99

# for i in range(10):
#     img = train_imgs[i].reshape((28,28))
#     plt.imshow(img, cmap="Greys")
#     plt.show()

def truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm((low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)

def sig(x):
    return 1/(1+np.exp(-x))

class NeuralNetwork:

    def __init__(self, no_in_nodes, no_out_nodes, no_hidden_nodes,lr):
        self.no_in_nodes = no_in_nodes;
        self.no_out_nodes = no_out_nodes;
        self.no_hidden_nodes = no_hidden_nodes;
        self.lr = lr;
        self.create_weight_matrix();

    def create_weight_matrix(self):
        rad = 1/np.sqrt(self.no_in_nodes)
        X = truncated_normal(0, 1, -rad, rad)
        self.wih = X.rvs((self.no_hidden_nodes, self.no_in_nodes))

        rad = 1/np.sqrt(self.no_hidden_nodes)
        X = truncated_normal(0, 1, -rad, rad)
        self.who = X.rvs((self.no_out_nodes, self.no_hidden_nodes))

    def train(self, input, target):
        input = np.array(input).T
        target = np.array(target).T

        out1 = sig(np.dot(self.wih, input))
        out2 = sig(np.dot(self.who, out1))

        error = target - out2

        #update weights
        tmp = error * out2 * (1.0-out2)
        tmp = self.lr*np.dot(tmp,out1.T)
        self.who += tmp;

        hidden_error = np.dot(self.who.T, error)
        tmp = hidden_error * out1 * (1.0-out1)
        tmp = self.lr*np.dot(tmp, input.T)
        self.wih += tmp



    def run(self, input):
        input = np.array(input).T
        out = sig(np.dot(self.wih, input))
        out = sig(np.dot(self.who, out))
        return out


    def evaluate(self, data, labels):
        corrects, wrongs = 0, 0
        for i in range(len(data)):
            res = self.run(data[i])
            res_max = res.argmax()
            if res_max == labels[i]:
                corrects += 1
            else:
                wrongs += 1
        return corrects, wrongs

ANN = NeuralNetwork(no_in_nodes = 784, no_out_nodes = 10, no_hidden_nodes = 100, lr = 0.1)

for i in range(len(train_imgs)):
    ANN.train(train_imgs[i], train_labels_one_hot[i])

for i in range(20):
    res = ANN.run(test_imgs[i])
    print(test_labels[i], np.argmax(res), np.max(res))

corrects, wrongs = ANN.evaluate(train_imgs, train_labels)
print("accruracy train: ", corrects / ( corrects + wrongs))
corrects, wrongs = ANN.evaluate(test_imgs, test_labels)
print("accruracy: test", corrects / ( corrects + wrongs))
