# -*- coding: utf-8 -*-

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 打开文本
text = open('D:\\开源项目\\深度有趣\\精简版\\03 词云\\03 词云\\xyj.txt').read()
# 生成对象
wc = WordCloud(font_path='D:\\开源项目\\深度有趣\\精简版\\03 词云\\03 词云\\Hiragino.ttf', width=800, height=600, mode='RGBA', background_color=None).generate(text)

# 显示词云
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()

# 保存到文件
wc.to_file('wordcloud2.png')