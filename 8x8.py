import numpy as np
import cv2
img=np.zeros((800,800,3))
img[0:100,0:100]=255,255,255
img[0:100,200:300]=255,255,255
img[0:100,400:500]=255,255,255
img[0:100,600:700]=255,255,255


img[100:200,100:200]=255,255,255
img[100:200,300:400]=255,255,255
img[100:200,500:600]=255,255,255
img[100:200,700:800]=255,255,255

img[200:300,0:100]=255,255,255
img[200:300,200:300]=255,255,255
img[200:300,400:500]=255,255,255
img[200:300,600:700]=255,255,255

img[300:400,100:200]=255,255,255
img[300:400,300:400]=255,255,255
img[300:400,500:600]=255,255,255
img[300:400,700:800]=255,255,255

img[400:500,0:100]=255,255,255
img[400:500,200:300]=255,255,255
img[400:500,400:500]=255,255,255
img[400:500,600:700]=255,255,255

img[500:600,100:200]=255,255,255
img[500:600,300:400]=255,255,255
img[500:600,500:600]=255,255,255
img[500:600,700:800]=255,255,255

img[600:700,0:100]=255,255,255
img[600:700,200:300]=255,255,255
img[600:700,400:500]=255,255,255
img[600:700,600:700]=255,255,255

img[700:800,100:200]=255,255,255
img[700:800,300:400]=255,255,255
img[700:800,500:600]=255,255,255
img[700:800,700:800]=255,255,255
cv2.imshow('chess board8*8',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
