import os
import cv2
import dlib
import face_recognition
from datetime import date

import numpy as np
from .models import Students , Attendence , Groups
# pwd = os.path.dirname(__file__)

def shape_to_np(shape, dtype="int"):
    # Initialize the list of (x, y)-coordinates
    coords = np.zeros((shape.num_parts, 2), dtype=dtype)

    # Loop over the facial landmarks and convert them to a 2-tuple of (x, y)-coordinates
    for i in range(0, shape.num_parts):
        coords[i] = (shape.part(i).x, shape.part(i).y)

    # Return the list of (x, y)-coordinates
    return coords


            
def auto_attendance():
    all_users = Students.objects.values('id')
    ids_list = [item['id'] for item in all_users]
    for user_id in ids_list:
        user = Students.objects.get(pk=user_id)
        att_user = Attendence.objects.filter(user_id=user).last()
        if att_user is None:
            try:
                Attendence.objects.create(user_id=user, date=date.today(), status=False)
                print('Auto attendance added for', user.username)
            except Exception as e:
                print('func 1: Error adding attendance:', str(e))
        elif att_user.date != date.today() and att_user is not None:
            try:
                Attendence.objects.create(user_id=user, date=date.today(), status=False)
                print('Auto attendance added for', user.username)
            except Exception as e:
                print('func 2: Error adding attendance:', str(e))
        else:
            print('User', user.username, ' already exists(in auto)!')

class VideoCamera:
    def __init__(self):
        self.detector = dlib.get_frontal_face_detector() # type: ignore
        self.cap = cv2.VideoCapture(1)
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml') # type: ignore
        self.generate_frames_and_check_faces()
        # face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        # eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        # self.cwd = os.getcwd()
        
        dat_path="face_recog_app/shape_predictor_68_face_landmarks.dat"
        
        # self.full_dat_path = os.path.join(cwd, dat_path) # type: ignore
        self.predictor = dlib.shape_predictor(dat_path) # type: ignore
        # self.pwd = os.path.dirname(__file__)
        # self.dat_path2="C:\Users\oqilj\OneDrive\Desktop\Intalim Face detect\face recog 2\face_recog\face_recog_app\shape_predictor_68_face_landmarks.dat"
        # self.predictor = dlib.shape_predictor(pwd+dat_path)
        self.EYE_AR_THRESH = 0.2
        self.EYE_AR_CONSEC_FRAMES =1

        # Initialize variables
        self.COUNTER = 0
        self.TOTAL = 0
        
    
    # Eye aspect ratio (EAR) calculation function
    def eye_aspect_ratio(self,eye):
        # Compute the euclidean distances between the two sets of vertical eye landmarks
        A = np.linalg.norm(eye[1] - eye[5])
        B = np.linalg.norm(eye[2] - eye[4])
        # Compute the euclidean distance between the horizontal eye landmarks
        C = np.linalg.norm(eye[0] - eye[3])
        # Compute the eye aspect ratio
        ear = (A + B) / (2.0 * C)
        return ear

    
        
    # def check_liveness(self,face):
    #     # Calculate the variance of pixel intensities within the face region
    #     variance = cv2.Laplacian(face, cv2.CV_64F).var()
    #     print("********************Liveness varian****************************")
    #     print(variance) 
    #     print("*******************Liveness varian*****************************")   
    #     return variance > 100
        

    def attendance(self, name):
        auto_attendance()
        user = Students.objects.filter(username=name).first()
        ids = user.id if user else print("User does not exist") # type: ignore
        users = Attendence.objects.filter(user_id=ids).last()
        if users:
            if ids is not None and users.status == False:
                try:
                    users.status = True
                    users.save()
                    print('Attendance added for', name)
                except Exception as e:
                    print('class inner: Error adding attendance:', str(e))
            else:
                print('User', name, 'is already in the database')

    def generate_frames_and_check_faces(self):
        # Initialize variables
        # global COUNTER
        # COUNTER = 0
        # TOTAL = 0
        
        
        l_start = 36
        l_end = 42
        r_start = 42
        r_end = 48
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.detector(gray)

            for face in faces:
                x, y, w, h = face.left(), face.top(), face.width(), face.height()
                center = (x + w // 2, y + h // 2)
                radius = int((w + h) // 3)
                cv2.circle(frame, center, radius, (0, 255, 0), 2)
                
                 # Detect facial landmarks
                shape = self.predictor(gray, face) # type: ignore
                shape = shape_to_np(shape)  # type: ignore

                # Extract the left and right eye coordinates
                left_eye = shape[l_start:l_end] # type: ignore
                right_eye = shape[r_start:r_end] # type: ignore

                # Calculate eye aspect ratio for each eye
                left_ear = self.eye_aspect_ratio(left_eye) # type: ignore
                right_ear = self.eye_aspect_ratio(right_eye) # type: ignore

                # Average the eye aspect ratio for both eyes
                ear = (left_ear + right_ear) / 2.0

                # Draw the eyes region
                left_eye_hull = cv2.convexHull(left_eye)
                right_eye_hull = cv2.convexHull(right_eye)
                cv2.drawContours(frame, [left_eye_hull], -1, (0, 255, 0), 1)
                cv2.drawContours(frame, [right_eye_hull], -1, (0, 255, 0), 1)
                print(ear)
                # Check if the eye aspect ratio is below the threshold
                if ear <= self.EYE_AR_THRESH: # type: ignore
                    self.COUNTER += 1
                    print("****************************Total func****************")
                    print(self.COUNTER)
                    print(self.EYE_AR_CONSEC_FRAMES)
                    print("****************************Total func****************")
                else:
                    if self.COUNTER >= self.EYE_AR_CONSEC_FRAMES: # type: ignore
                        self.TOTAL += 1
                    self.COUNTER = 0
                print(self.TOTAL)
                # Display the eye aspect ratio on the frame
                cv2.putText(frame, f"EAR: {ear:.2f}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                
                
                face_region=gray[y:y + h, x:x + w]
                # Eye detection for liveness check
                eyes = self.eye_cascade.detectMultiScale(face_region, scaleFactor=1.1, minNeighbors=5)
                
                # Check for liveness
                # is_real = self.check_liveness(face_region)
                # print("*******************Is_real*****************************")
                # print(is_real)
                # print(eyes)
                # print(len(eyes))
                # print("*******************Is_real*****************************")
                # color = (0, 255, 0) if is_real else (0, 0, 255)
                # cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                if len(eyes) >= 2:  # Assuming at least 2 eyes detected for liveness
                    face_locations = [(y, x + w, y + h, x)]
                    face_encodings = face_recognition.face_encodings(frame, face_locations)

                # face_locations = [(y, x + w, y + h, x)]
                # face_encodings = face_recognition.face_encodings(frame, face_locations)

                    if len(face_encodings) >= 1:
                        face_encoding = face_encodings[0]
                        students = Students.objects.all()
                        for item in students:
                            self.reference_image_path = f'media/{item.image}'
                            self.reference_image = cv2.imread(self.reference_image_path)
                            self.reference_encoding = face_recognition.face_encodings(self.reference_image)[0]
                            usernames = item.username

                            results_user = face_recognition.compare_faces([self.reference_encoding], face_encoding)
                            if results_user[0] == True and self.TOTAL>=1:
                                self.name = usernames
                                self.attendance(usernames)
                            else:
                                self.name = "Not found"

                            text_position = (x + 10, y + 280)
                            cv2.putText(frame, self.name, text_position, cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)

            # Display the total number of blinks
                all=f"Blinks: {self.TOTAL}"
                cv2.putText(frame, all , (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
                self.TOTAL=0
            

            # # Display the frame
            # cv2.imshow("Frame", frame)
            
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
