import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np


N = 10
noisy_percent = 0.1
noisy_sample = int(N * noisy_percent)

def gen_sample1():
    # generate N samples of 2D between [-1, 1]
    x1 = np.random.uniform(low=-1.0, high=1.0, size=N)
    x2 = np.random.uniform(low=-1.0, high=1.0, size=N)
    y = np.sign(x1**2 + x2**2 - 0.6)

    # choose noisy sample
    noisy_index = np.random.choice(N, noisy_sample)
    for i in range(noisy_sample):
        y[noisy_index[i]] = y[noisy_index[i]] * -1

    x0 = np.zeroes((N, 1))
    x = np.hstack((x0, x1.reshape(N, 1), x2.reshape(N,1)))


def percectron(x, y):
    ##