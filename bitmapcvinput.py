import numpy as np
import cv2
import time
import sys
img = cv2.imread("image.png") #dimensions: 2036 × 1664
# cv2.imshow('input', img)


#32 x 32



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
def concat_vh(list_2d):
    return cv2.vconcat([cv2.hconcat(list_h)  
                        for list_h in list_2d]) 
# image resizing 
img1_s = cv2.resize(img1, dsize = (0,0), 
                    fx = 0.5, fy = 0.5) 
  
# function calling 
img_tile = concat_vh([[img1_s, img1_s, img1_s], 
                      [img1_s, img1_s, img1_s], 
                      [img1_s, img1_s, img1_s]]) 
# show the output image 
cv2.imshow('concat_vh.jpg', img_tile)

#method 2: make 2d list and append all gridx for one column into that array, and then vstack (vertically combines) them into one image at the end.
#repeat this for each column of gridx (you can constantly intialize the same 2d array to [0][0]) and then finally hstack (horizontally) them into a tile of images.

img12 = np.hstack((img1, img2))
img34 = np.hstack((img3, img4))
result = np.vstack((img12, img34))


cv2.waitKey(0)



# # top_section = image[:half_height, :]
# bottom_section = image[half_height:, :]

# cv2.imshow('Top', top_section)
# cv2.imshow('Bottom', bottom_section)

# cv2.waitKey(0)

