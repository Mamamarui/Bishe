# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 10:46:47 2018

@author: Shaoruizhi
"""

import tensorflow as tf  
import numpy as np
  
sess = tf.Session()  
#  
## First, load meta graph and restore weights  
#saver = tf.train.import_meta_graph('model.ckpt.meta')  
#saver.restore(sess, tf.train.latest_checkpoint('./'))  
#  
## Second, access and create placeholders variables and create feed_dict to feed new data  
#graph = tf.get_default_graph()  
#w1 = graph.get_tensor_by_name('w1:0')  
#feed_dict = {w1:[7]}  
#  
## Access the op that want to run  
#op_to_restore = graph.get_tensor_by_name('op_to_restore:0')  
#  
#print (sess.run(op_to_restore, feed_dict))     # ouotput: [6. 14.]

saver = tf.train.Saver()
saver.restore(sess, ".\model.ckpt")
data=np.array([[7]])
graph = tf.get_default_graph() 
prob_op = graph.get_operation_by_name('y')
prediction = graph.get_tensor_by_name('y:0')
result = sess.run(prediction,feed_dict={x: data})