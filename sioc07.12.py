import numpy as np
import math
import cv2

def interpolation_function (x, y, img_original):
    x1 = math.floor(x)
    y1 = math.floor(y)
    v1 = img_original[x1][y1]

    x2 = math.ceil(x)
    y2 = math.floor(y)
    v2 = img_original[x2][y2]

    x3 = math.floor(x)
    y3 = math.ceil(y)
    v3 = img_original[x3][y3]

    x4 = math.ceil(x)
    y4 = math.ceil(y)
    v4 = img_original[x4][y4]

    #print("---", x1, y1, v1, x2, y2, v2, x3, y3, v3, x4, y4, v4  )

    if x2==x1:
        v12 = v1
    else:
        v12 = v1 + ((x - x1)*(v2-v1) / (x2-x1))

    if x4 == x3:
        v34 = v3
    else:
        v34 = v3 + ((x-x3)*(v4-v3) / (x4-x3))

    if y3 == y1:
        value_for_xy = v12
    else:
        value_for_xy = v12 + ((y - y1)*(v34-v12) / (y3-y1))

    return value_for_xy.astype(np.uint8)



img = cv2.imread('zebry.jfif')[:,:,0]

img_rotated = np.zeros_like(img)

wide = img_rotated.shape[0]
height = img_rotated.shape[1]

alfa = np.pi / 4

macierz_obrotu = np.array([[np.cos(-alfa), -np.sin(-alfa)], [np.sin(-alfa), np.cos(-alfa)]])


for i in range(0, img_rotated.shape[0]-1):
    for j in range (0, img_rotated.shape[1]-1):

        x1 = i - wide/2
        y1 = j - height/2

        macierz_po_obrocie = macierz_obrotu @ np.array([x1, y1])

        x_stare = macierz_po_obrocie[0] + wide/2
        y_stare = macierz_po_obrocie[1] + height/2

        if x_stare >= img.shape[0]-1 or y_stare >= img.shape[1]-1:
            img_rotated[i][j] = img[img.shape[0]-1][img.shape[1]-1]
        else:
            img_rotated[i][j] = interpolation_function(x_stare, y_stare, img)

        #print(x_stare, y_stare)
        #print(img[2][799])
        #print(interpolation_function(x_stare, y_stare, img))




#print(img_rotated.shape)
#print(img_rotated)

cv2.imshow("original", img)
cv2.imshow('rotated', img_rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
