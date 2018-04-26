# -*- coding: utf-8 -*-
#"""Functions for downloading and reading MNIST data."""
#from __future__ import absolute_import
#from __future__ import division
#from __future__ import print_function
#
## pylint: disable=unused-import
#import gzip
#import os
#import tempfile
#
#import numpy
#from six.moves import urllib
#from six.moves import xrange  # pylint: disable=redefined-builtin
#import tensorflow as tf
#from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets
## pylint: enable=unused-import

import tensorflow.examples.tutorials.mnist.input_data as input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
import tensorflow as tf
import numpy as np

#None表示此张量的第一个维度可以是任何长度的，784表示每张图展平层784位的向量
x=tf.placeholder(tf.float32,[None,784])
#Variable代表一个可修改的张量。
#W的维度是[784，10]，因为我们想要用784维的图片向量乘以它以得到一个10维的证据值向量，
#每一位对应不同数字类。b的形状是[10]，所以我们可以直接把它加到输出上面。
W=tf.Variable(tf.zeros([784,10]))
b=tf.Variable(tf.zeros([10]))
#预测值通过softmax函数与真实标签y关联在一起,y是一个10维的行向量，分别是各个位置的概率
y=tf.nn.softmax(tf.matmul(x,W)+b)
#真实标签y_
y_=tf.placeholder("float",[None,10])
#计算交叉熵
cross_entropy = -tf.reduce_sum(y_*tf.log(y))
#使用梯度下降法以0.01的学习率最小化交叉熵
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
#运算前初始化变量（必须进行）
init = tf.initialize_all_variables()
#模型需要在session中启动
sess = tf.Session()
sess.run(init)
#训练模型，训练次数1000次，每次随机抓取100个数据
for i in range(1000):
  batch_xs, batch_ys = mnist.train.next_batch(100)
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
#模型评估  
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
print("准确率：\n",sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
data=np.zeros((1,784))
data[0,:]=batch_xs[0,:]
result=sess.run(y,feed_dict={x:data})
print(tf.argmax(result,1))