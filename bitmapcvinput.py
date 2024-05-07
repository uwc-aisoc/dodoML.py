import numpy as np
import cv2
import time
import sys
img = cv2.imread("image.png") #dimensions: 2036 × 1664
# cv2.imshow('input', img)


#32 x 32
def concat_vh(list_2d):
    return cv2.vconcat([cv2.hconcat(list_h)  
                        for list_h in list_2d])  

for width in range(0, 63):
    for height in range(0, 32):
        bottomH = height*32
        topH = bottomH+32
        bottomW = width*32
        topW = bottomW+32
        gridx = img[bottomH:topH, bottomW:topW]
        cv2.imshow('grid'+str(height)+str(width), gridx)
        cv2.waitKey(0)
        
        
       

#method 1: images can be combined using both cv2.hconcat() and cv2.vconcat() in tile form using a 2D list.
#you might need to fix the indentation a little bit

  
# function calling 
img_tile = concat_vh([[img, img, img], 
                      [img, img, img], 
                      [img, img, img]) 
# show the output image 
cv2.imshow('concat_vh.jpg', img_tile)


cv2.waitKey(0)



# # top_section = image[:half_height, :]
# bottom_section = image[half_height:, :]

# cv2.imshow('Top', top_section)
# cv2.imshow('Bottom', bottom_section)

# cv2.waitKey(0)

