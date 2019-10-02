# tensorflow examples for Movie reviews classification

# Imports
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import tensorflow as tf
from tensorflow import keras
import tensorflow_datasets as tfds
tfds.disable_progress_bar()

import numpy as np
print('tf versions is: ', tf.__version__)

# load IMDB datasets
(train_data, test_data), info = tfds.load('imdb_reviews/subwords8k',
                                          split = (tfds.Split.TRAIN, tfds.Split.TEST),
                                          as_supervised=True,
                                          with_info=True)

# Try the encoder
encoder = info.features['text'].encoder
print('Vocabulary size: {}'.format(encoder.vocab_size))

# This text encoder will reversibly encode any string

sample_string = 'Hello World.'
encoded_string = encoder.encode(sample_string)
print('Encoded string is {}.'.format(encoded_string))
original_string = encoder.decode(encoded_string)
print('The original string: "{}"'.format(original_string))
assert original_string == sample_string

# The encoder encodes the string by breaking it into subwords
for ts in encoded_string:
  print ('{} ----> {}'.format(ts, encoder.decode([ts])))

# Explore the data
for train_example, train_label in train_data.take(1):
    print('Encoded text:', train_example[:10].numpy())
    print('Label:', train_label.numpy())
print('Original text is: ', encoder.decode(train_example))

# Prepare the data for training
BUFFER_SIZE = 1000
train_batches = train_data.shuffle(BUFFER_SIZE).padded_batch(32, train_data.output_shapes)
test_batches = test_data.padded_batch(32, train_data.output_shapes)
for example_batch, label_batch in train_batches.take(2):
    print("Batch shape:", example_batch.shape)
    print("label shape:", label_batch.shape)

# Build the model
model = keras.Sequential([
                          keras.layers.Embedding(encoder.vocab_size, 16),
                          keras.layers.GlobalAveragePooling1D(),
                          keras.layers.Dense(1, activation='sigmoid')])

model.summary()

# Loss
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
# train the model
history = model.fit(train_batches,
                    epochs=10,
                    validation_data=test_batches,
                    validation_steps=30)

# Evaluate the model
loss, accuracy = model.evaluate(test_batches)

print("Loss: ", loss)
print("Accuracy: ", accuracy)
