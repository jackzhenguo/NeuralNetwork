import numpy as np
import matplotlib.pyplot as plt


with open(r'mnist/mnist_train.csv', 'r') as datafile:
    line = datafile.readline()
    i = 1
    while line and i < 50:
        all_values = line.split(',')
        label = all_values[0]
        img_array = np.asfarray(all_values[1:]).reshape((28, 28))
        # plt.axis('off')
        plt.imshow(img_array, cmap='Greys')
        filename = 'mnist/mnist_images/test' + str(i) +\
                   '_' + label + '.png'
        plt.savefig(filename)
        i += 1
        line = datafile.readline()