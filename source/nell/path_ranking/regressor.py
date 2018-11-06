from __future__ import absolute_import, division, print_function

import tensorflow as tf
from tensorflow import keras
import sys

import numpy as np

print(tf.__version__)

PATHS = sys.argv[1]

(train_data, train_labels), (test_data, test_labels) = tf.contrib.learn.datasets.base.load_csv_without_header(filename=PATHS, target_dtype=np.int, features_dtype=np.float32)

# Shuffle the training set
order = np.argsort(np.random.random(train_labels.shape))
train_data = train_data[order]
train_labels = train_labels[order]

print("Training set: {}".format(train_data.shape))  # 404 examples, 13 features
print("Testing set:  {}".format(test_data.shape))   # 102 examples, 13 features