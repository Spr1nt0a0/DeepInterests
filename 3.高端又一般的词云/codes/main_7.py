# -*- coding: utf-8 -*-

from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba.analyse

# 打开文本
text = open('D:\\开源项目\\深度有趣\\精简版\\03 词云\\03 词云\\xyj.txt').read()

# 提取关键词和权重
freq = jieba.analyse.extract_tags(text, topK=200, withWeight=True)
print(freq[:20])
freq = {i[0]: i[1] for i in freq}

# 生成对象
mask = np.array(Image.open("D:\\开源项目\\深度有趣\\精简版\\03 词云\\03 词云\\color_mask.png"))
wc = WordCloud(mask=mask, font_path='D:\\开源项目\\深度有趣\\精简版\\03 词云\\03 词云\\Hiragino.ttf', mode='RGBA', background_color=None).generate_from_frequencies(freq)

# 从图片中生成颜色
image_colors = ImageColorGenerator(mask)
wc.recolor(color_func=image_colors)

# 显示词云
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()

# 保存到文件
wc.to_file('wordcloud7.png')