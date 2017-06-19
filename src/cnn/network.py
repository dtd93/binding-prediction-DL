import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv3D, MaxPooling3D
from keras.optimizers import Adam
from keras.utils import np_utils
from keras import backend as K


#TODO, accuracy, recall, rogC


def runCNN(boxSize, nFilters, kernelSize, nClases, nEpoch, batchSize, X, Y):


    X_train = np.array(X)
    Y_train = np.array(Y)
    Y_train = Y_train.reshape((-1, 1))
    # (1 channel, 25 rows, 25 cols, 25 of depth)
    input_shape = (boxSize, boxSize, boxSize,8)
    # Init
    model = Sequential()

    # 3D Convolution layer
    model.add(Conv3D(nFilters,kernelSize,
                            input_shape=input_shape,
                            activation='relu'))

    # Fully Connected layer
    model.add(Flatten())
    model.add(Dense(1, activation='relu'))
    model.add(Dropout(0.5))

    # Softmax Layer
    model.add(Dense(nClases))
    model.add(Activation('sigmoid'))

    # Compile
    model.compile(loss='binary_crossentropy',
            optimizer= Adam(), metrics=['accuracy'])

    # Fit network
    model.fit(X_train, Y_train, batch_size= batchSize, epochs=nEpoch, verbose=1)