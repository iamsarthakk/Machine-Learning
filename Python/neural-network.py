import numpy as np

def sigm( x , deriv = False):
    if(deriv):
        return x*(1-x)

    return 1/(1+np.exp(-x))

X = np.array([[0,0,1],
             [0,1,1],
             [1,0,1],
             [1,1,1]])

y = np.array([[0],
              [1],
              [1],
              [0]])
np.random.seed(1)
w1 = 2*np.random.random((3,4))-1
w2 = 2*np.random.random((4,1))-1

for i in range(6000):
    l0=X
    l1=sigm(np.dot(l0,w1))
    l2=sigm(np.dot(l1,w2))

    l2_error = y-l2

    if(i%10000):
        print "Error"+str(np.mean(np.abs(l2_error)))

        l2_delta = l2_error*sigm(l2,deriv=True)
        l1_error = l2_delta.dot(w2.T)
        l1_delta = l1_error*sigm(l1,deriv = True)

        w2 += l1.T.dot(l2_delta)
        w1 += l0.T.dot(l1_delta)

print "output after training"
print l2
