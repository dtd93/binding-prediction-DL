import numpy as np


def generateTrainingData(boxSize):
    X_train, Y_train = [], []

    i=0
    for filename in os.listdir(os.path.join(os.getcwd(), 'models')):
        with open(os.path.join(os.getcwd(), 'models', filename)) as f:
            file = f.readlines()
            json_file = '\n'.join(file)
            content = json.loads(json_file)
            occupancy = content['model']['occupancy']
            form = []
            for value in occupancy:
                form.append(int(value))
            final_model = [ [ [ 0 for i in range(boxSize) ]
                                for j in range(boxSize) ]
                                for k in range(boxSize) ]
            a = 0
            for i in range(boxSize):
                for j in range(boxSize):
                    for k in range(boxSize):
                        final_model[i][j][k] = form[a]
                        a = a + 1
            X_train.append(final_model)
            Y_train.append(content['model']['label'])

    X_train = np.array(X_train)
    Y_train = np.array(Y_train)