#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2 
import numpy as np 
import matplotlib.pyplot as plt


# In[19]:


image = cv2.imread(r'C:\Users\LENOVO\Desktop\New folder\Images\tmp_9.png') 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
cv2.imshow("gray",gray)
cv2.waitKey(0)


# In[20]:


def findContr(image):
    edged = cv2.Canny(gray, 1, 2) 
    contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
    return contours


# In[21]:


def checkinside(image):
    for i in findContr(image):
        check = cv2.pointPolygonTest((i),(320,250),False)
        if check == 1:
            distance = abs(int(cv2.pointPolygonTest((i),(320,250),True)))
            if distance is not []:
                return distance
print(checkinside(image))
chek=checkinside(image)


# In[22]:


img=cv2.Canny(image,1,1)
point=[]
TARGET = (320,250)
def find_nearest_white(img, target):
    nonzero = cv2.findNonZero(img)
    distances = np.sqrt((nonzero[:,:,0] - TARGET[0]) ** 2 + (nonzero[:,:,1] - TARGET[1]) ** 2)
    nearest_index = np.argmin(distances)
    point.append(nonzero[nearest_index][0][0])
    point.append(nonzero[nearest_index][0][1])
    return nonzero[nearest_index]


print (find_nearest_white(img, TARGET))
x=point[0]
y=point[1]


# In[23]:


contour1=findContr(image)
a=[]
if chek == None:
    x=320
    y=250
for i in contour1:
    
    dist = abs(cv2.pointPolygonTest(i,(x,y),True))
    a.append(dist)

def second_smallest(numbers):
    m1, m2 = float('inf'), float('inf')
    for x in numbers:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return m2
print("nearest distance is :",second_smallest(a))


# In[ ]:




