import wordcloud
from numpy import array
from jieba import cut
import matplotlib.pyplot as plt
from matplotlib import patches
from PIL import Image

def  make_mask(shape, dpi):
    mask_fig = plt.figure(figsize=(6,6),facecolor='w' ,dpi=dpi)
    mask_ax = mask_fig.add_subplot(111)
    xy_center =(0.5,0.5)
    if(shape == 'circle' or shape == 'c'):
        mask_ax.add_patch(patches.Circle(xy_center,0.5))
    elif(shape =='ellipse' or shape =='e'):
        mask_ax.add_patch(patches.Ellipse(xy_center,1, 0.75))
    elif (shape == 'rectangle' or shape =='r'):
        mask_ax.add_patch(patches.Rectangle((0,0.15), 1, 0.75))
    elif (shape == 'square' or shape =='s'):
        mask_ax.add_patch(patches.Rectangle((0,0), 1, 1))
    else :
        shape = int(shape)
        mask_ax.add_patch(patches.RegularPolygon(xy_center,shape,0.5))
    mask_ax.axis('off')
    mask_fig.savefig('mask.png')
    mask=array(Image.open('mask.png'))
    plt.close()
    return mask

def jieba_split(text_addr):
    text = open(text_addr,encoding='utf-8').read()
    text_split =''.join(cut(text))
    return text_split
def cloud_generate(text_addr,shape = 'e',colormap = 'Set2',dpi = 200 ,output_addr = 'wordcloud_output.png',stopwords = None):
    my_wordcloud=wordcloud.WordCloud(height =(6*dpi),width =make_mask(shape,dpi),font_path = 'simhei.ttf',stopwords=stopwords,background='white').generate(jieba_split(text_addr))
    cloud_fig =plt.figure(figsize=(6,6),dpi=dpi)
    cloud_ax=cloud_fig.add_subplot(111)
    cloud_ax.imshow(my_wordcloud.recorlor(colormap=colormap))
    cloud_ax.axis('off')
    cloud_fig.savefig('output_addr')
    return

if __name__ =='__mian__':
    cloud_generate(text_addr='/Users/bytednce/Desktop/text.text',shape='e',colormap='Set2',dpi=400)