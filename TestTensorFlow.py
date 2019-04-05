# https://github.com/fchollet/deep-learning-with-python-notebooks/blob/master/2.1-a-first-look-at-a-neural-network.ipynb

# from keras.datasets import mnist
# #
# # (train_images, train_labels), (test_images, test_labels) = mnist.load_data()

import os
import tensorflow as tf
import keras
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

keras.__version__

hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print(train_images.shape)
print(train_labels)
print(test_images.shape)

network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
network.add(layers.Dense(10, activation='softmax'))
network.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

print('training: '+str(train_images[0]))

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

network.fit(train_images, train_labels, epochs=1, batch_size=128)

test_loss, test_acc = network.evaluate(test_images, test_labels)

print('test_acc:', test_acc)