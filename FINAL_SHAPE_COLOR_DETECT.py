#COlOR DETECTING

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# Define object specific variables
dist = 0
focal = 450
pixels = 30
width = 8


# find the distance from then camera
def get_dist(rectange_params, image):
    # find no of pixels covered
    pixels = rectange_params[1][0]
    # calculate distance
    dist = (width * focal) / pixels
    dist1 = round(dist,2)
    # Wrtie n the image
    image = cv2.putText(image, 'Distance from Camera in CM :', org, font,
                        1, color, 2, cv2.LINE_AA)

    image = cv2.putText(image, str(dist1), (110, 50), font,
                        fontScale, color, 1, cv2.LINE_AA)
    return image

#basic constants for opencv Functs
kernel = np.ones((3,3),'uint8')
font = cv2.FONT_HERSHEY_SIMPLEX
org = (0,20)
fontScale = 0.6
color = (0, 0, 255)
thickness = 2

def rescaleframe(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width,height)
    return cv2.resize(frame, dimension, interpolation = cv2.INTER_AREA)

while True:
    font = cv2.FONT_HERSHEY_SIMPLEX
    _, frame = cap.read()
    img = cv2.GaussianBlur(frame, (15, 15), 0)
    #img = cv2.medianBlur(frame, 15)
    hsv_frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    low_red = np.array([0, 100, 100])
    high_red = np.array([5, 255, 255])
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    low_green = np.array([36, 50, 70])
    high_green = np.array([89, 255, 255])
    low_yellow = np.array([22, 93, 0])
    high_yellow = np.array([45, 255, 255])
    low = np.array([0, 42, 0])
    high = np.array([179, 255, 255])

    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)
    yellow_mask = cv2.inRange(hsv_frame, low_yellow, high_yellow)
    yellow = cv2.bitwise_and(frame, frame, mask=yellow_mask)
    mask = cv2.inRange(hsv_frame, low, high)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours1, _ = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours2, _ = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours3, _ = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
        x = approx.ravel()[0]
        y = approx.ravel()[1]

        if area > 400:
            rect = cv2.minAreaRect(cnt)
            img = get_dist(rect, frame)

            #cv2.drawContours(frame, [approx], 0, (0, 40, 255), 2)
            M = cv2.moments(cnt)
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"]/M["m00"])

            #cv2.circle(frame, (cx,cy), 7, (255,255,255), -1)
            #cv2.putText(frame, "red", (cx-20, cy-20), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 40, 255), 3)
            b = 1
            if len(approx) == 3:
                #cv2.putText(frame, "Triangle", (x, y), font, 1.5, (0, 0, 0), 3)
                a = 3
            elif len(approx) == 4:
                #cv2.putText(frame, "Rectangle", (x, y), font, 1.5, (0, 0, 0), 3)
                a = 4
            elif 6 < len(approx):
                #cv2.putText(frame, "Circle", (x, y), font, 1.5, (0, 0, 0), 3)
                a = 5

    for cnt in contours1:
        area = cv2.contourArea(cnt)
        approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
        x = approx.ravel()[0]
        y = approx.ravel()[1]

        if area > 400:
            rect = cv2.minAreaRect(cnt)
            img = get_dist(rect, frame)

            #cv2.drawContours(frame, [approx], 0, (0, 176, 24), 2)
            M = cv2.moments(cnt)
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"]/M["m00"])

            #cv2.circle(frame, (cx,cy), 7, (255,255,255), -1)
            #cv2.putText(frame, "green", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 176, 24), 3)
            b = 2
            if len(approx) == 3:
                #cv2.putText(frame, "Triangle", (x, y), font, 1.5, (0, 0, 0), 3)
                a = 3
            elif len(approx) == 4:
                #cv2.putText(frame, "Rectangle", (x, y), font, 1.5, (0, 0, 0), 3)
                a = 4
            elif 6 < len(approx):
                #cv2.putText(frame, "Circle", (x, y), font, 1.5, (0, 0, 0), 3)
                a = 5

    for cnt in contours2:
        area = cv2.contourArea(cnt)
        approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
        x = approx.ravel()[0]
        y = approx.ravel()[1]

        if area > 400:
            rect = cv2.minAreaRect(cnt)
            img = get_dist(rect, frame)

            #cv2.drawContours(frame, [approx], 0, (198, 43, 0), 2)
            M = cv2.moments(cnt)
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"]/M["m00"])

            #cv2.circle(frame, (cx,cy), 7, (255,255,255), -1)
            #cv2.putText(frame, "blue", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (198, 43, 0), 3)
            b = 3
            if len(approx) == 3:
                #cv2.putText(frame, "Triangle", (x, y), font, 1.5, (0, 0, 0), 3)
                a = 3
            elif len(approx) == 4:
                #cv2.putText(frame, "Rectangle", (x, y), font, 1.5, (0, 0, 0), 3)
                a = 4
            elif 6 < len(approx):
                #cv2.putText(frame, "Circle", (x, y), font, 1.5, (0, 0, 0), 3)
                a = 5

    for cnt in contours3:
        area = cv2.contourArea(cnt)
        approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
        x = approx.ravel()[0]
        y = approx.ravel()[1]

        if area > 400:
            rect = cv2.minAreaRect(cnt)
            img = get_dist(rect, frame)

            #cv2.drawContours(frame, [approx], 0, (0, 237, 255), 2)
            M = cv2.moments(cnt)
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"]/M["m00"])

            #cv2.circle(frame, (cx,cy), 7, (255,255,255), -1)
            #cv2.putText(frame, "yellow", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 237, 255), 3)
            b = 4
            if len(approx) == 3:
                #cv2.putText(frame, "Triangle", (x, y), font, 1.5, (0, 0, 0), 3)
                a = 3
            elif len(approx) == 4:
                #cv2.putText(frame, "Rectangle", (x, y), font, 1.5, (0, 0, 0), 3)
                a = 4
            elif 6 < len(approx):
                #cv2.putText(frame, "Circle", (x, y), font, 1.5, (0, 0, 0), 3)
                a = 5

    if((a==3) and (b==1)):
        cv2.drawContours(frame, [approx], 0, (0, 40, 255), 2)
        cv2.putText(frame, "Triangle", (x, y), font, 1.5, (0, 0, 0), 3)
        cv2.circle(frame, (cx,cy), 7, (255,255,255), -1)
        cv2.putText(frame, "red", (cx-20, cy-20), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 40, 255), 3)
        c = 1;
        print("Re trai")
    elif((a==4) and (b==2)):
        cv2.putText(frame, "Rectangle", (x, y), font, 1.5, (0, 0, 0), 3)
        cv2.drawContours(frame, [approx], 0, (0, 176, 24), 2)
        cv2.circle(frame, (cx,cy), 7, (255,255,255), -1)
        cv2.putText(frame, "green", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 176, 24), 3)
        c = 2;
        print("Re phai")
    elif((a==5) and (b==3)):
        cv2.putText(frame, "Circle", (x, y), font, 1.5, (0, 0, 0), 3)
        cv2.drawContours(frame, [approx], 0, (198, 43, 0), 2)
        cv2.circle(frame, (cx,cy), 7, (255,255,255), -1)
        cv2.putText(frame, "blue", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (198, 43, 0), 3)
        c = 3;
        print("Dung")
    elif((a==4) and (b==3)):
        cv2.putText(frame, "Rectangle", (x, y), font, 1.5, (0, 0, 0), 3)
        cv2.drawContours(frame, [approx], 0, (198, 43, 0), 2)
        cv2.circle(frame, (cx,cy), 7, (255,255,255), -1)
        cv2.putText(frame, "blue", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (198, 43, 0), 3)
        c = 4;
        print("Tien len")
    elif((a==3) and (b==4)):
        cv2.drawContours(frame, [approx], 0, (0, 237, 255), 2)
        cv2.putText(frame, "Triangle", (x, y), font, 1.5, (0, 0, 0), 3)
        cv2.circle(frame, (cx,cy), 7, (255,255,255), -1)
        cv2.putText(frame, "yellow", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 237, 255), 3)
        c = 5;
        print("Lui xuong")
    cv2.imshow("IMAGE_DETECT", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyAllWindows()

