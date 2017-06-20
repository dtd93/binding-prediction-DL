import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv3D, MaxPooling3D
from keras.optimizers import Adam
from keras.layers.advanced_activations import ELU

from keras.utils import np_utils
from keras import backend as K
from cnn import netFunctionalities as nf


#TODO, accuracy, recall, rogC


def runCNN(boxSize, nFilters, kernelSize, nClases, nEpoch, batchSize, X, Y, datafolder):


    X_train = np.array(X)
    Y_train = np.array(Y)
    Y_train = Y_train.reshape((-1, 1))
    # (1 channel, 25 rows, 25 cols, 25 of depth)
    input_shape = (boxSize, boxSize, boxSize,8)
    # Init
    model = Sequential()

    # 3D Convolution layer
    model.add(Conv3D(nFilters,kernelSize, border_mode='same',
                            input_shape=input_shape))

    # Fully Connected layer

    model.add(ELU())
    model.add(Conv3D(48,4))
    model.add(ELU())
    model.add(MaxPooling3D(pool_size=(2, 2, 2)))
    model.add(Dropout(0.25))
    model.add(Conv3D(64,4, border_mode='same'))
    model.add(ELU())
    model.add(Conv3D(96,4, border_mode='same'))
    model.add(ELU())
    model.add(MaxPooling3D(pool_size=(2, 2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(256))
    model.add(ELU())
    model.add(Dropout(0.5))

    # Softmax Layer
    model.add(Dense(nClases))
    model.add(Activation('sigmoid'))

    # Compile
    model.compile(loss='binary_crossentropy',
            optimizer= Adam(), metrics=['accuracy', recall])

    # Fit network
    model.fit(X_train, Y_train, batch_size= batchSize, epochs=nEpoch, verbose=1)
    
    
    nf.evaluateModel(model, X_train, Y_train)
    
    nf.saveModelToFile(datafolder, model)

def recall(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    recall = true_positives / (possible_positives + K.epsilon())
    return recall