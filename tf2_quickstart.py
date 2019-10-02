## Quick Start for tensorflow 2
# imports
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import tensorflow as tf
from tensorflow.keras.layers import Dense, Flatten, Conv2D
from tensorflow.keras import Model

# load MNIST dataset
mnist = tf.keras.datasets.mnist 
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# normalization
x_train, x_test = x_train / 255.0, x_test / 255.0

# add a channels dimension
x_train = x_train[..., tf.newaxis]
# tf.newaxis to expand dimension t0 [dims, 1]
x_test = x_test[...,tf.newaxis]

# use tf.data to batch and shuffle the data
train_ds = tf.data.Dataset.from_tensor_slices((x_train, y_train)).shuffle(10000).batch(32)
test_ds = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(32)

# Build the tf.keras model 
class MyModel(Model):
	def __init__(self):
		super(MyModel, self).__init__()
		# Python super function can refer to the superclass implicitly.
		self.conv1 = Conv2D(32, 3, activation = 'relu')
		self.flatten = Flatten()
		self.d1 = Dense(128, activation = 'relu')
		self.d2 = Dense(10, activation = 'softmax')


	def call(self, x):
		x = self.conv1(x)
		x = self.flatten(x)
		x = self.d1(x)
		return self.d2(x)


# create an instance fo the model
model = MyModel()
# Choose an optimizer and loss function for training
# instance from classes
loss_object = tf.keras.losses.SparseCategoricalCrossentropy()
optimizer = tf.keras.optimizers.Adam()

# metrics 
train_loss = tf.keras.metrics.Mean(name = 'train_loss')
# args: name, dtype
train_accuracy = tf.keras.metrics.SparseCategoricalCrossentropy(name = 'train_accuracy')
# args: name, dtype
#  reset_states(): Resets all of the metric state variables.
# result(): Computes and returns the metric value tensor.
# __new__: Create and return a new object.
# update_state: Accumulates metric statistics.
#  __call__(
#     y_true,
#     y_pred,
#     sample_weight=None
# )
test_loss = tf.keras.metrics.Mean(name = 'test_loss')
test_accuracy = tf.keras.metrics.SparseCategoricalCrossentropy(name = 'test_accuracy')

# train the model 
# A cool new feature of tf.function is AutoGraph, which lets you write graph code using natural Python syntax
@tf.function
def train_step(images, labels):
# Operations are recorded if they are executed within this context manager and at least one of their inputs is being "watched".
# Trainable variables automatically watched.
# batch_jacobian
# gradient
# jacobian
# reset()
# stop_recording()
# watch(tensor)
# watched_variables()
  with tf.GradientTape() as tape:
    predictions = model(images)
    loss = loss_object(labels, predictions)
  # compute gradients
  gradients = tape.gradient(loss, model.trainable_variables)
  optimizer.apply_gradients(zip(gradients, model.trainable_variables))
  train_loss(loss)
  train_accuracy(labels, predictions)

# test the model 
@tf.function
def test_step(images, labels):
	predictions = model(images)
	t_loss = loss_object(labels, predictions)

	test_loss(t_loss)
	test_accuracy(labels, predictions)

# main function
EPOCHS = 5

for epoch in range(EPOCHS):
	for images, labels in train_ds:
		train_step(images, labels)

	for test_images, test_labels in test_ds:
		test_step(test_images, test_labels)

	template = 'Epoch {}, Loss: {}, Accuracy: {}, Test Loss: {}, Test Accuracy: {}'

	print(template.format(epoch+1, train_loss.result(),
		train_accuracy.result()*100,
		test_loss.result(),
		test_accuracy.result()))
	# reset the metrics for the next epoch
	train_loss.reset_states()
	train_accuracy.reset_states()
	test_loss.reset_states()
	test_accuracy.reset_states()
