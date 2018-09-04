import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from tftf.datasets import load_mnist
from tftf.layers import Dense, Activation, BatchNormalization, Dropout, \
    Conv2D, MaxPooling2D, GlobalAveragePooling2D
from tftf.models import Model


if __name__ == '__main__':
    '''
    Load data
    '''
    mnist = load_mnist(train_test_split=False)

    n = len(mnist.data)
    N = 30000
    indices = np.random.permutation(range(n))[:N]

    X = mnist.data[indices]
    X = X / 255.0
    y = mnist.target[indices]

    train_X, test_X, train_y, test_y = train_test_split(X, y)

    '''
    Build model
    '''
    model = Model()
    model.add(Conv2D(input_dim=(28, 28, 1),
                     kernel_size=(3, 3, 20),
                     padding='valid'))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(Dropout(0.3))
    model.add(MaxPooling2D())
    model.add(Conv2D(kernel_size=(3, 3, 50),
                     padding='valid'))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(Dropout(0.3))
    model.add(MaxPooling2D())
    model.add(GlobalAveragePooling2D())
    model.add(Dense(1024))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(10))
    model.add(Activation('softmax'))
    model.compile()

    model.describe()

    '''
    Train model
    '''
    model.fit(train_X, train_y)

    '''
    Test model
    '''
    print(model.accuracy(test_X, test_y))
