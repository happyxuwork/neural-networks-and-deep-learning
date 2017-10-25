# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''
import mnist_loader
import network

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
print("training data")
print(type(training_data))
print(len(training_data))
print(training_data[0][0].shape)
print(training_data[0][1].shape)
#
# net = network.Network([784,30,10])
# net.SGD(training_data,30,10,3.0,test_data=test_data)


'''
how to use defaultdict to give a default to some collection
'''
# from collections import defaultdict
# #the normal way to handel
# strings = ('puppy', 'kitten', 'puppy', 'puppy',
#            'weasel', 'puppy', 'kitten', 'puppy')
# count = {}
# for kw in strings:
#     count[kw] = count.setdefault(kw, 0) + 1
# print(count)
#
# #use the defaultdict
# strings1 = ('puppy', 'kitten', 'puppy', 'puppy',
#            'weasel', 'puppy', 'kitten', 'puppy')
# counts = defaultdict(lambda: 0)  # 使用lambda来定义简单的函数
# for s in strings1:
#     counts[s] += 1
# print(counts)
# print(defaultdict.__missing__.__doc__) #this is a good to see the doc for help
