import cv2

def diffres(t0, t1, t2):
    # t paremetrisine atadığımız saniyede bir aldığı görüntüyü diferansiyel                                                                    görüntüye atamasını sağlıyor
  
    d1= cv2.absdiff(t2, t1)
    d2 = cv2.absdiff(t1, t0)

    return cv2.bitwise_and(d1, d2)

cam = cv2.VideoCapture(0)
namedWindow = "Difarensiyel görüntü"

cv2.namedWindow(namedWindow, cv2.WINDOW_AUTOSIZE)

#kameraya bağlanıp görüntü alınmasını sağlayan kodumuz

a = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

b = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

c = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

while True:

    cv2.imshow(namedWindow, diffres(a,b,c) )
    a = b
    b = c
    c = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    key = cv2.waitKey(10)
    if key == 0xFF & ord("q"):

        cv2.destroyWindow(winName)
        break
