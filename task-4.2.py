#Task 4.2
#Take 2 images and crop some part of both the images and swap it.

import cv2
import numpy as np
image= cv2.imread("smile.jpg")
image.shape
image2=cv2.imread("sad.png")
image2.shape
image2=cv2.resize(image2, [480,480])
image2.shape
cv2.imshow('smile',image)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imshow('sad',image2)
cv2.waitKey()
cv2.destroyAllWindows()
#Here, I have cropped to show a part of the first image 
cropped1= image[60:380,200:450]
#Here, I have swapped the cropped part of the first image with the second image
image2[60:380,200:450] = cropped1
cv2.imshow("Swapping1", image2)
cv2.waitKey()
cv2.destroyAllWindows()
image2 = cv2.imread("sad.png")
#Here, I have cropped a part of the second image 
cropped2 = image2[60:380,200:450]
#Here, I have swapped the cropped part of the second image with the first image.
image[60:380,200:450] = cropped2
cv2.imshow("Swapping2", image)
cv2.waitKey()
cv2.destroyAllWindows()
#Task Complete
