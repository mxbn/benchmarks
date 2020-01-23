import os
os.system('pip install --upgrade tensorflow')

import time
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.utils import to_categorical

if __name__ == '__main__':
    
    print('tf version: %s' % tf.__version__)
    
    n_rows = 1000000
    n_cols = 1000

    np.random.seed(0)
    x = np.random.random((n_rows,n_cols))
    d = np.sqrt(x.sum(axis=1)**(1/2))
    half = np.percentile(d, 50)
    y = to_categorical(np.where(d < half, 0, 1), 2)

    split = int(0.8*x.shape[0])
    train_x = x[:split]
    train_y = y[:split]
    valid_x = x[split:]
    valid_y = y[split:]

    model = tf.keras.Sequential()
    model.add(layers.Dense(x.shape[1], activation='relu', input_shape=(x.shape[1],)))
    model.add(layers.Dense(2, activation='softmax'))

    if tf.__version__[0] == '2':
        optimizer = tf.keras.optimizers.Adam(0.01)
    else:
        optimizer = tf.train.AdamOptimizer(0.01)

    model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

    t0 = time.time()
    model.fit(train_x, train_y, epochs=5, validation_data=(valid_x, valid_y), batch_size=32, verbose=0)
    print('%d sec' % (time.time() - t0))
