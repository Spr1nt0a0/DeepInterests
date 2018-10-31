# 2 准备工作
## 2.1 简介
在个人电脑上，搭建编程所需要的各项环境。
## 2.2 Anaconda
一个涵盖了python，pip以及python包的软件。
## 2.3 pycharm
一个简洁清爽的编辑器。
## 2.4 运行代码
运行代码的三种办法：
* 使用编辑器编写代码，并在编辑器中运行；
* 使用编辑器编写代码，并在命令行中运行；
* 使用Jupyter Notebook编写代码并运行。
## 2.5 安装包
可以用pip或者conda安装python包。
## 2.6 文件路径
windows上的文件路径以左斜杠拼接。  
而Mac和Linux上的文件以又斜杠拼接。
## 2.7 中文编码
在windows上读写文本文件时，最好指定编码为utf8，尤其时文件中包括中文时。
## 2.8 深度学习框架
tensorflow和keras都是很流行的深度学习框架，tensorflow提供了更加底层的API，keras封装性更高，以theano和tensorflow等底层框架为backend。
## 2.9 GPU
CNN等神经网络模型使用GPU训练更快，有条件的话可以使用GPU，不然只能使用CPU进行训练，相应的安装tensorflow的GPU版本。  
如果是英伟达的GPU，那么还要安装和配置CUDN和CuGDNN，注意版本兼容的问题。
