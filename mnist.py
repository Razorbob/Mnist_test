import input_data
mnist = input_data.read_data_sets("/Datasets/", one_hot=True)

import tensorflow as tf

#Hyperparameters
learning_rate = 0.01
training_iteration = 30
batch_size = 100
display_step = 2

