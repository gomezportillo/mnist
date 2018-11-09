#!/usr/bin/python3
# -*- coding:utf-8 -*-

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
from keras import backend
print("Using TensorFlow v{}".format(tf.__version__))

# Helper libraries
import numpy
import matplotlib.pyplot as plt
import time

#Local libraries
from aux import render_image
from aux import render_imagelist

# Downloading MNIST dataset from keras
(train_images, train_labels), (test_images, test_labels) = keras.datasets.mnist.load_data()

# Getting unique values from labels, sorting them and storing
class_names = list(set(train_labels))

# Prepocessing
## Normalising datasets before feeding to the neural network
train_images = train_images / 255.0
test_images = test_images / 255.0

# Building the model
NODES_DENSE_1 = 128
NODES_DENSE_2 = 10

LAYER_1 = keras.layers.Flatten(input_shape=(28, 28))
LAYER_2 = keras.layers.Dense(NODES_DENSE_1, activation=tf.nn.relu)
LAYER_3 = keras.layers.Dense(NODES_DENSE_2, activation=tf.nn.softmax)

# https://keras.io/models/sequential/
model = keras.Sequential([ LAYER_1, LAYER_2, LAYER_3 ])

# Compiling the model
model.compile(optimizer=tf.train.AdamOptimizer(),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model with the train images
EPOCHS = 5

start = time.time()
model.fit(train_images, train_labels, epochs=EPOCHS)
end = time.time()
print("Training time: {}s".format(end - start))

# Evaluate the accuracy of the model with the train images
train_loss, train_acc = model.evaluate(train_images, train_labels)
acc = 'Train accuracy: {}%'.format(train_acc*100)
loss = 'Train loss: {}%'.format(train_loss*100)
print(acc)
print(loss)

score = model.evaluate(train_images, train_labels)
print(score)

# Evaluate the accuracy of the model with the test images
test_loss, test_acc = model.evaluate(test_images, test_labels)
acc = 'Test accuracy: {}%'.format(test_acc*100)
loss = 'Test loss: {}%'.format(test_loss*100)
print(acc)
print(loss)

# Predicting the classes of all test images
prediction = model.predict(test_images)
result = numpy.argmax(prediction, axis=-1)
print(result)
