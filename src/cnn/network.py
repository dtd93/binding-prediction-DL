import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution3D, MaxPooling3D
from keras.optimizers import SGD
from keras.utils import np_utils
from keras import backend as K



def runCNN(boxSize, nFilters, kernelSize, nClases, nEpoch, batchSize, X, Y):


    X_train = np.array(X)
    Y_train = np.array(Y)

    # (1 channel, 25 rows, 25 cols, 25 of depth)
    input_shape = (boxSize, boxSize, boxSize, 8)

    # Init
    model = Sequential()

    # 3D Convolution layer
    model.add(Convolution3D(nFilters, boxSize, boxSize, boxSize,
                            input_shape=input_shape,
                            activation='relu'))

    # Fully Connected layer
    model.add(Flatten())
    model.add(Dense(128, init='normal', activation='relu'))
    model.add(Dropout(0.5))

    # Softmax Layer
    model.add(Dense(nClases, init='normal'))
    model.add(Activation('softmax'))

    # Compile
    model.compile(loss='categorical_crossentropy',
                optimizer=SGD())

    # Fit network
    model.fit(X_train, Y_train, batch_size= batchSize, nb_epoch=nEpoch, verbose=1)