# 3 高端又一般的词云
## 3.1 简介
词云是一种数据呈现方式：
* 不会的时候，感觉很厉害、很高大上；
* 会用了之后，感觉到哪都看到别人在用。
掌握用Python实现词云的方法。
## 3.2 准备
安装包。  
> pip install wordcloud matplotlib jieba PIL
## 3.3 一个简单的例子
WordCloud()可选的参数:
* font_path：可用于指定字体路径，包括otf和ttf;
* width：词云的宽度，默认为400;
* height：词云的高度，默认为200;
* mask：蒙版，可用于定制词云的形状;
* min_font_size：最小字号，默认为4;
* max_font_size：最大字号，默认为词云的高度;
* max_words：词的最大数量，默认为200;
* stopwords：将被忽略的停用词，如果不指定则使用默认的停用词词库;
* background_color：背景颜色，默认为black;
* mode：默认为RGB模式，如果为RGBA模式且background_color设为None，则背景将透明。
代码参考code/main_1.py 。 
由于英文单词之间有分隔，因此大多不需要额外的处理。
## 3.4 中文词云
中文一般需要经过分词处理，先看下不分词的效果。  
以《西游记》为例，可以看到结果中会出现各种双字、三字和四字等，但很多并不是合理的词语。  
代码参考code/main_2.py。  
这次我们先用jieba进行中文分词，可以看到生成的词云里，基本上都是合理的词语了。  
代码参考code/main_3.py。  
## 3.5 使用蒙版
这里将mask翻译为蒙版，是因为感觉它和Photoshop中蒙版的作用很类似。  
使用蒙版之后，可以根据提供的蒙版图片，生成指定形状的词云。  
代码参考code/main_4.py。
## 3.6 颜色
词云的颜色可以从蒙版中抽取，使用ImageColorGenerator()即可。  
代码参考code/main_5.py。  
当然也可以设置为纯色，增加一个配色函数即可。  
代码参考code/main_6.py。
## 3.7 精细控制
如果希望精细地控制词云中出现的词，以及每个词的大小，可以尝试generate_from_frequencies()，包括两个参数：
* frequencies：一个字典，用于指定词和对应的大小；
* max_font_size：最大字号，默认为None。
generate() = process_text() + generate_from_frequencies()。  
以下用jieba提取出关键词和权重，再以此绘制词云。  
代码参考code/main_7.py。

