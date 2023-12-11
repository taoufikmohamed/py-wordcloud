import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import  numpy as np
import PIL.Image

# Load the data
text=open('text.txt','r').read()
pymask= np.array(PIL.Image.open('R.jpeg'))
# Generate a word cloud
colormap=ImageColorGenerator(pymask)
wc = WordCloud(stopwords=STOPWORDS,mask=pymask, 
              background_color="white",
              contour_color="black",
               contour_width=1,
               min_font_size=1,
               max_words=300).generate(text)
wc.recolor(color_func=colormap)
plt.figure(figsize = (16, 16), facecolor = None)
plt.imshow(wc)
plt.axis("off")
plt.tight_layout(pad = 0)
plt.show()

