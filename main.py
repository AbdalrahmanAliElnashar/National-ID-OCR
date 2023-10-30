import cv2
import numpy as np
import utlis
import easygui
import cvzone

# Width and height of the image
widthImg  = 800
heightImg = 600

# The Image
img = cv2.imread(easygui.fileopenbox()) # CHOOSE THE IMAGE
img = cv2.resize(img, (widthImg, heightImg)) # RESIZE IMAGE
imgBlank = np.zeros((heightImg,widthImg, 3), np.uint8) # CREATE A BLANK IMAGE FOR TESTING DEBUGING IF REQUIRED
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # CONVERT IMAGE TO GRAY SCALE
imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1) # ADD GAUSSIAN BLUR

# Check For Warping
w = input('Do you want to warp the image? (y/n): ')
if w == 'y':
    
    utlis.initializeTrackbars()
    # EDGEs TRACKBAR: Trackbar to define Card Edges to apply warping to the image
    while True:
        thres = utlis.valTrackbars()  # GET TRACKBAR VALUES FOR THRESHOLDS
        imgThreshold = cv2.Canny(imgBlur, thres[0], thres[1])  # APPLY CANNY EDGE DETECTION
        cv2.imshow("EDGE Detection", imgThreshold)
        
        # Wait for a key event and check if it's the 'Esc' key (27)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            break
        elif key == ord('s'):  # Press 's' to save the image
            cv2.imwrite('thresholded_image.jpg', imgThreshold)
            print("Image saved as 'thresholded_image.jpg'")

    # Dilation and Erosion
    kernel = np.ones((5, 5))
    imgDial = cv2.dilate(imgThreshold, kernel, iterations=2) # APPLY DILATION
    imgThreshold = cv2.erode(imgDial, kernel, iterations=1)  # APPLY EROSION




    # WARP PRESPECTIVE
    ## FIND ALL COUNTOURS
    imgContours = img.copy() # COPY IMAGE FOR DISPLAY PURPOSES
    imgBigContour = img.copy() # COPY IMAGE FOR DISPLAY PURPOSES
    contours, hierarchy = cv2.findContours(imgThreshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # FIND ALL CONTOURS
    cv2.drawContours(imgContours, contours, -1, (0, 255, 0), 10) # DRAW ALL DETECTED CONTOURS

    # FIND THE BIGGEST COUNTOUR
    biggest, maxArea = utlis.biggestContour(contours) # FIND THE BIGGEST CONTOUR

    if biggest.size != 0:
        biggest=utlis.reorder(biggest)
        cv2.drawContours(imgBigContour, biggest, -1, (0, 255, 0), 20) # DRAW THE BIGGEST CONTOUR
        imgBigContour = utlis.drawRectangle(imgBigContour,biggest,2)
        pts1 = np.float32(biggest) # PREPARE POINTS FOR WARP
        pts2 = np.float32([[0, 0],[widthImg, 0], [0, heightImg],[widthImg, heightImg]]) # PREPARE POINTS FOR WARP
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        img = cv2.warpPerspective(img, matrix, (widthImg, heightImg))

        stackedImage = cvzone.stackImages([img, imgGray, imgThreshold, imgContours, imgBigContour, img], 3, 0.5)

    else:
        stackedImage = cvzone.stackImages([img, imgGray, imgThreshold, imgContours, img, img], 3, 0.5)
        pass

    cv2.imshow("original",stackedImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    pass


################ OCR ################
import pytesseract as pyt
pyt.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
utlis.initializeTrackbars()


img = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Results are good at threshold: 166 - 242
# THRESHOLD TRACKBAR
while True:
    thres = utlis.valTrackbars()  # GET TRACKBAR VALUES FOR THRESHOLDS
    _, imgThreshold = cv2.threshold(gray, thres[0], thres[1], cv2.THRESH_BINARY_INV)
    cv2.imshow("Threshold", imgThreshold)
    cv2.imwrite('test_NID_7.jpg', imgThreshold)
    
    # Wait for a key event and check if it's the 'Esc' key (27)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break


# OCR
text = pyt.image_to_string(imgThreshold)
print(text)


# remove special characters
import re
text = re.sub(r'[^a-zA-Z0-9]', ' ', text)
#print(text)


# Split the string into individual words
words = text.lower().split()
print(words)


# Store the words in a dictionary
d = {}
for word in words:
    if word == 'surname':
        d[word] = words[words.index(word)+1]
    if word == 'name' or word == 'names':
        d[word] = words[words.index(word)+1]
    if word == 'nationality':
        d[word] = words[words.index(word)+1]
    if word == 'sex':
        d[word] = words[words.index(word)+1]
    if word == 'number':
        d['identity number'] = words[words.index(word)+1]
    if word == 'date':
        d[word] = words[words.index(word)+3]+' '+words[words.index(word)+4]+' '+words[words.index(word)+5]
    if word == 'country':
        d[word] = words[words.index(word)+3]
    if word == 'status':
        d[word] = words[words.index(word)+1]
    
#print(d)


import pandas as pd
# Create a list of dictionaries
df = pd.DataFrame(d, index=[1])
print(df)
df.to_csv('NID_Information.csv', index=False)

cv2.waitKey(0)
cv2.destroyAllWindows()

