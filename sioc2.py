import cv2
import numpy as np

###funckja interpolujaca kolor niebieski
def blue_interpolation(blue_inter):
    rows = blue_inter.shape[0]
    col = blue_inter.shape[1]

    #interpolacja w wierszach
    for i in range(1,rows,2):
        for j in range(0, col,2):
            blue_inter[i][j] = blue_inter[i][j+1]

    #interpolacja w kolumnach
    for i in range(0,col-1):
        for j in range(0,rows-1,2):
            blue_inter[j][i] = blue_inter[j+1][i]


    return blue_inter

###funckja interpolujaca kolor niebieski
def red_interpolation (red_inter):
    rows = red_inter.shape[0]
    col  = red_inter.shape[1]

    for i in range(0,rows,2):
        for j in range(1,col,2):
            red_inter[i][j] = red_inter[i][j-1]

    for i in range(0,col,):
        for j in range(1,rows,2):
            red_inter[j][i] = red_inter[j-1][i]

    return red_inter

###Funckja interpolujaca kolor zielony
def green_interpolation (green_inter):
    rows = green_inter.shape[0]
    col = green_inter.shape[1]

    for i in range(0,rows,2):
        for j in range(0,col,2):
            green_inter[i][j] = green_inter[i][j+1]

    for i in range(1,rows,2):
        for j in range(1,col,2):
            green_inter[i][j] = green_inter[i][j-1]

    return green_inter


#Loading the image
img = cv2.imread('kotek.jpg')
###order: Blue, Green, Red

###Rozdzielamy obraz na kolory
Blue, Green, Red = cv2.split(img)

###Tworzymy tablice filtrów
CFA_B = np.array([[0,0],[0,1]])
CFA_G = np.array([[0,1],[1,0]])
CFA_R = np.array([[1,0],[0,0]])

###Rozszerzamy tablice filtrów CFA do rozmiarów obrazu
repeat_rows = img.shape[0] // 2 +1
repeat_col = img.shape[1] // 2 +1

CFA_B_e = np.tile(CFA_B, (repeat_rows, repeat_col,))[:img.shape[0], :img.shape[1]]
CFA_G_e = np.tile(CFA_G, (repeat_rows, repeat_col,))[:img.shape[0], :img.shape[1]]
CFA_R_e = np.tile(CFA_R, (repeat_rows, repeat_col,))[:img.shape[0], :img.shape[1]]

###Tworzymy tablice kolorow, ktore bedziemy interpolowac
blue_cfa = Blue * CFA_B_e
green_cfa = Green * CFA_G_e
red_cfa = Red * CFA_R_e

###Interpolujemy tablice kolorow
blue_channel = blue_interpolation(blue_cfa)
green_channel = green_interpolation(green_cfa)
red_channel = red_interpolation(red_cfa)

###Tworzymy tablice ktora bedzie obrazem
img_inter = cv2.merge((blue_channel, green_channel, red_channel))

###Zmieniamy typ danych w tablicy na uint8 (taki typ danych przyjmuje funkcja cv2.imshow ktora tworzy i wyswietla obraz
img_inter_uint8 =  img_inter.astype(np.uint8)


###Wyswietlanie obrazu oryginalnego i po interpolacji
cv2.imshow("original", img)
cv2.imshow("interpolated", img_inter_uint8)
cv2.waitKey(0)
cv2.destroyAllWindows()