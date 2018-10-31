# -*- coding: utf-8 -*-

from wordcloud import WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba

# 打开文本
text = open('D:\\开源项目\\深度有趣\\精简版\\03 词云\\03 词云\\xyj.txt').read()

# 中文分词
text = ' '.join(jieba.cut(text))
print(text[:100])

# 生成对象
mask = np.array(Image.open("D:\\开源项目\\深度有趣\\精简版\\03 词云\\03 词云\\black_mask.png"))
wc = WordCloud(mask=mask, font_path='D:\\开源项目\\深度有趣\\精简版\\03 词云\\03 词云\\Hiragino.ttf', mode='RGBA', background_color=None).generate(text)

# 显示词云
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()

# 保存到文件
wc.to_file('wordcloud4.png')