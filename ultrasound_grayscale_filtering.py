# importing OpenCV(cv2) module 
import cv2 
  
# Save image in set directory 
# Read RGB image 
img = cv2.imread('cropped.jpg')  
  
# Output img with window name as 'image' 
cv2.imshow('image', img)  
cv2.waitKey(0)         

# Destroying present windows on screen 
cv2.destroyAllWindows()  

print('Image size {}'.format(img.size))
print('Maximum grayscale value in this image {}'.format(img.max()))
print('Minimum grayscale value in this image {}'.format(img.min()))

print('Type of the image : ' , type(img))
print()
print('Shape of the image : {}'.format(img.shape))
print('Image Hight {}'.format(img.shape[0]))
print('Image Width {}'.format(img.shape[1]))
print('Dimension of Image {}'.format(img.ndim))

#print(img[1000,13,1])
#p = 0
#for i in range(0,img.shape[0]):
#    p = p + 1;

q = 0
for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        if img[i,j,1] > 127:
            q = q + 1

#0 black 255 white
#printing out percentage of majority white part
print((float(q)/float(img.size))*100)

#no way an algorithm better than https://www.ncbi.nlm.nih.gov/pubmed/30530325 be used without using machine learning
