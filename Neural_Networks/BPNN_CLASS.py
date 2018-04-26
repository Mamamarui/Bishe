import random
import numpy as np
import tensorflow as tf

class train():
    def __init__(self,att,labels):
        self.m=att.shape[0]
        self.n=att.shape[1]
        self.att=att
        self.labels=labels
    def next_batch(self,n):
        if n>self.m :
            print("错误：随机抽取的数据个数超过数据总数。")
        else:
            x=np.zeros((n,self.n),int)
            yshape=list(self.labels.shape)
            del yshape[0]
            y=np.zeros(tuple(yshape),int)
            for i in range(0,n):
                r=random.randint(0,self.m-1)
                for j in range(0,self.n):
                    x[i,j]=self.att[r,j]
                y=self.labels[r,:,:]
#                y=np.transpose(y)
            return x,y

class test():
    def __init__(self,att,labels):
        self.num=labels.shape[0]
        self.att=att
        self.labels=labels
        
class sample():
     def __init__(self,tr_att,tr_labels,ts_att,ts_labels):
         self.train=train(tr_att,tr_labels)
         self.test=test(ts_att,ts_labels)

         
tr_labels=np.array([[[0,0,0,0,0,1]],[[0,0,0,0,1,0]],[[0,0,0,1,0,0]],\
                    [[0,0,1,0,0,0]],[[1,0,0,0,0,0]]])
tr_att=np.array([[5],[3],[2],[1],[0]])
ts_labels=np.array([[0,1,0,0,0,0]])
ts_att=np.array([[4]])

a=sample(tr_att,tr_labels,ts_att,ts_labels)

x=tf.placeholder(tf.float32,[None,1],name='x')
W=tf.Variable(tf.zeros([1,6]),name='W')
b=tf.Variable(tf.zeros([6]),name='b')
y=tf.nn.softmax(tf.matmul(x,W)+b,name='y')
y_=tf.placeholder("float",[None,6],name='y_')

cross_entropy = -tf.reduce_sum(y_*tf.log(y))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
#init = tf.initialize_all_variables()
#init=tf.global_variables_initializer

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(1000):
    batch_xs, batch_ys =a.train.next_batch(2)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
  
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
print("准确率：\n",sess.run(accuracy, feed_dict={x: a.test.att, y_: a.test.labels}))

#saver = tf.train.Saver()
#model_path = "./model.ckpt"
#saver.save(sess, model_path)
data=np.array([[2],[1]])
result = sess.run(y, feed_dict={x: data})
print(result)