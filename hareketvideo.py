import cv2

def diffres(t0, t1, t2):

    d1= cv2.absdiff(t2, t1)
    d2 = cv2.absdiff(t1, t0)

    return cv2.bitwise_and(d1, d2)

cam = cv2.VideoCapture('görüntü işleme.mp4')
namedWindow = "Difarensiyel görüntü"

cv2.namedWindow(namedWindow, cv2.WINDOW_AUTOSIZE)



a = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

b = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

c = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)


while True:

    resim_1 = diffres(a, b, c)
    cv2.imshow("Windows_1", resim_1)
    # Üstte bulunmakta olan iki satır hareket algilayan videoyu göstermektedir.
    ret, threshold_resim = cv2.threshold(resim_1, 50, 255, cv2.THRESH_BINARY)
    cv2.imshow(namedWindow,threshold_resim)
    # Üstte bulunmakta olan iki satır, eşik değeri ile değiştirilmiş resmi göstermektedir.

    a = b
    b = c
    c = cv2.cvtColor(cam.read()[1],cv2.COLOR_RGB2GRAY)
    key = cv2.waitKey(40)

    if key == 0xFF & ord("q"):

#     cv2.destroyWindow()
     break
