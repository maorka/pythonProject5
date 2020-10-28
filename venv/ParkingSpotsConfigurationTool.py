from PIL import Image
from pylab import *
import matplotlib.pyplot as plt

#read image to array
im = array(Image.open('shalom_alichem_night_keren.jpg'))

# plot the image
imshow(im)

# some points
#x = [100,100,400,400]
#y = [200,500,200,500]

# # plot the points with red star-markers
# plot(x,y,'r*')
#
# # line plot connecting the first two points
# plot(x[:2],y[:2])
#axes = plt.gca()
#axes.set_xlim([0,255])
#axes.set_ylim([0,255])
# add title and show the plot
title('Plotting: "shalom_alichem_night_keren.jpg"')
show()
