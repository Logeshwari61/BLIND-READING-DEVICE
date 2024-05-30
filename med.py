import cv2
from PIL import Image
import pytesseract
import pyttsx3
pytesseract.pytesseract.tesseract_cmd='c:/Tesseract-OCR/Tesseract.exe'
en=pyttsx3.init()
en.setproperty('rate', 80)
cap = cv2.VideoCapture(0)

while True:
 #print("ok")
ret, frame = cap.read()
cv2.imshow('frame' ,frame)
cv2.imwrite("1.jpg",frame)
img = Image.open ("1.jpg")
text = pytesseract.image_to_string(img, config="")
print (text)
en.say(text)
en.runAndWait ()
if cv2.waitKey(1) & 0xFF == ord('q'):
 break

cap.release()
cv2.destroyAllWindows ()
