import cv2
import os
import numpy as np
import time

imgpath = os.getenv("IMAGEPATH")


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def capture_face(imgname, filename=imgpath):
    
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow("Press 'c' to capture", frame)
            
            key = cv2.waitKey(1)
            if key == ord('c'):
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                
                for (x, y, w, h) in faces:
                    face = frame[y:y+h, x:x+w]
                    save_path = os.path.join(filename, imgname)
                    cv2.imwrite(save_path, face)
                    print(f"Image saved at: {save_path}")
                break
        else:
            print("Failed to capture image")
            break
    cap.release()
    cv2.destroyAllWindows()




# def verify(imagename, filename=imgpath):
    
#     # capture_face(img_name)
#     img_name = filename + "/" + imagename
#     captured_image = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)
#     cap = cv2.VideoCapture(0)
#     face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#     while True:
#         ret, frame = cap.read()
#         if ret:
#             cv2.imshow("Press 'c' to capture", frame)
            
#             key = cv2.waitKey(1) & 0xFF
#             if key == ord('c'):
#                 gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#                 faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                
#                 for (x, y, w, h) in faces:
#                     face = frame[y:y+h, x:x+w]
#                     cv2.imwrite("C:/Users/verma/Downloads/attendance-log/attendance-log/app/new.png", face)
#                 break
#     new_image = cv2.imread("new.png", cv2.IMREAD_GRAYSCALE)

#     if captured_image is not None and new_image is not None:
#         # Resize images to the same size for comparison
#         print(f"enter{new_image}-----check{captured_image}")
#         captured_image = cv2.resize(captured_image, (100, 100))
#         new_image = cv2.resize(new_image, (100, 100))

#         captured_image = cv2.cvtColor(captured_image, cv2.COLOR_BGR2GRAY)
#         new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)

#         mse = np.mean((captured_image - new_image)**2)
#         threshold = 100  # Adjust the threshold as needed
#         is_similar = mse < threshold

#         print("Images are similar:", is_similar)
#         # difference = cv2.absdiff(captured_image, new_image)
#         # print(difference,"-----------------")
#         # result = not difference.any()
#         return True
    
#     return False

