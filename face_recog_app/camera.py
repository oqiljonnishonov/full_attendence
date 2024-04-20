# import cv2
# import dlib
# import face_recognition
# from datetime import date
# from .models import Users, Attendance
# from .models import Students , Attendence , Groups

# class VideoCamera:
#     def __init__(self):
#         self.detector = dlib.get_frontal_face_detector()
#         self.cap = cv2.VideoCapture(0)
#         self.load_reference_images()
        
#     def attendance(self , name):
#         user = Students.objects.filter(username=name).first()
#         att_user=Attendance.objects.filter(user_id=user).last()
#         if att_user is not None:
#             if att_user.date!=date.today():
#                 if user:
#                     new_attendance = Attendance(user_id=user.id, date=date.today(), status=False)
#                     try:
#                         new_attendance.save()
#                         print('Attendance added for', name)
#                     except Exception as e:
#                         print('Error adding attendance:', str(e))
#                 else:
#                     print('User', name, 'not found in the database')
#         else:
#             if user:
#                 new_attendance = Attendance(user_id=user.id, date=date.today(), status=False)
#                 try:
#                     new_attendance.save()
#                     print('Attendance added for', name)
#                 except Exception as e:
#                     print('Error adding attendance:', str(e))
#             else:
#                 print('User', name, 'not found in the database')

#     def load_reference_images(self):
#         self.students=Students.object.all()
#         # usernames_and_images = [(item["username"], item["image"]) for item in students]
#         # print("Usernames and Images:", usernames_and_images)
#         # for user_details in usernames_and_images:
#         for item in students:  #(item["username"], item["image"]) 
#             self.reference_image_path=item["image"]
#             self.reference_image = cv2.imread(self.reference_image_path)
#             self.reference_encoding = face_recognition.face_encodings(self.reference_image)[0]
#             self.name=item["username"]      
        
#         # self.name='o'
#         # self.reference_image_path_mine = "face_recognition_app\static\images\photo_of_mine.jpg"
#         # self.reference_image_mine = cv2.imread(self.reference_image_path_mine)
#         # self.reference_encoding_mine = face_recognition.face_encodings(self.reference_image_mine)[0]

#         # self.reference_image_path_friend = "face_recognition_app\static\images\picture_of_other.jpg"
#         # self.reference_image_friend = cv2.imread(self.reference_image_path_friend)
#         # self.reference_encoding_friend = face_recognition.face_encodings(self.reference_image_friend)[0]

#     def generate_frames(self):
#         while True:
#             ret, frame = self.cap.read()
#             if not ret:
#                 break

#             gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#             faces = self.detector(gray)

#             for face in faces:
#                 x, y, w, h = face.left(), face.top(), face.width(), face.height()
#                 center = (x + w // 2, y + h // 2)
#                 radius = int((w + h) // 3)
#                 cv2.circle(frame, center, radius, (0, 255, 0), 2)

#                 face_locations = [(y, x + w, y + h, x)]
#                 face_encodings = face_recognition.face_encodings(frame, face_locations)

#                 if len(face_encodings) > 0:
#                     face_encoding = face_encodings[0]
#                     def check_face(self):
#                         results_mine = face_recognition.compare_faces([self.reference_encoding_mine], face_encoding)
#                         results_friend = face_recognition.compare_faces([self.reference_encoding_friend], face_encoding)

#                         if any(results_mine):
#                             self.name = "Oqiljon Islomov"
#                             self.attendance("Oqiljon Islomov")
#                         elif any(results_friend):
#                             self.name = "Saidvali Bahriddinov"
#                             self.attendance("Saidvali Bahriddinov")
#                         else:
#                             self.name = "Topilmadi..."
#                             # self.attendance("Topilmadi...")

#                         text_position = (x + 10, y + 280)
#                         cv2.putText(frame, self.name, text_position, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

#             ret, buffer = cv2.imencode('.jpg', frame)
#             frame = buffer.tobytes()
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
# def auto_attendence():
#     all_users=Users.objects.values('id')
#     print(all_users)
#     ids_list = [item['id'] for item in all_users]
#     print(ids_list)
#     for user_id in ids_list:
#         user=Users.objects.get(pk=user_id)
#         att_user=Attendance.objects.filter(user_id=user_id).last()
#         if att_user.date!=date.today():
#             try:
#                 Attendance.objects.create(user_id=user_id,date=date.today(),status=False)
#                 print('Attendance added for', user.username)
#             except Exception as e:
#                 print('Error adding attendance:', str(e))
#         else:
#             print('User', user.username, ' already axist !')






# import cv2
# import dlib
# import face_recognition
# from datetime import date
# from .models import Students , Attendence , Groups

# class VideoCamera:
#     def __init__(self):
#         self.detector = dlib.get_frontal_face_detector()
#         self.cap = cv2.VideoCapture(0)
#         self.generate_frames_and_check_faces()
        
#     def attendance(self , name):
#         user = Students.objects.filter(username=name).first()
#         att_user=Attendence.objects.filter(user_id=user).last()
#         if att_user is not None:
#             if att_user.date!=date.today():
#                 if user:
#                     new_attendance = Attendence(user_id=user, date=date.today(), status=True)
#                     try:
#                         new_attendance.save()
#                         print('Attendance added for', name)
#                     except Exception as e:
#                         print('Error adding attendance:', str(e))
#                 else:
#                     print('User', name, 'not found in the database')
#         else:
#             if user:
#                 new_attendance = Attendence(user_id=user, date=date.today(), status=True)
#                 try:
#                     new_attendance.save()
#                     print('Attendance added for', name)
#                 except Exception as e:
#                     print('Error adding attendance:', str(e))
#             else:
#                 print('User', name, 'not found in the database')

#     def generate_frames_and_check_faces(self):
#         while True:
#             ret, frame = self.cap.read()
#             if not ret:
#                 break

#             gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#             faces = self.detector(gray)

#             for face in faces:
#                 x, y, w, h = face.left(), face.top(), face.width(), face.height()
#                 center = (x + w // 2, y + h // 2)
#                 radius = int((w + h) // 3)
#                 cv2.circle(frame, center, radius, (0, 255, 0), 2)

#                 face_locations = [(y, x + w, y + h, x)]
#                 face_encodings = face_recognition.face_encodings(frame, face_locations)

#                 if len(face_encodings) > 0:
#                     face_encoding = face_encodings[0]
#                     # media\images\Oqiljon_Islomov.JPG
#                     students=Students.objects.all()
#                     for item in students:  #(item["username"], item["image"]) 
#                         print('*******************************************')
#                         print(item.image)
#                         print(item.username)
#                         # print(item["image"])
#                         # print(item["username"])
#                         print(f'media/{item.image}')
#                         print('*******************************************')
#                         self.reference_image_path=f'media/{item.image}'
#                         self.reference_image = cv2.imread(self.reference_image_path)
#                         # self.reference_image = cv2.imread(item.image)
#                         self.reference_encoding = face_recognition.face_encodings(self.reference_image)[0]
#                         usernames=item.username
                        
#                         results_mine = face_recognition.compare_faces([self.reference_encoding], face_encoding)

#                         if any(results_mine):
#                             self.name = usernames
#                             self.attendance(usernames)
#                         else:
#                             self.name = "Topilmadi..."
                    
#                         text_position = (x + 10, y + 280)
#                         cv2.putText(frame, self.name, text_position, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

#             ret, buffer = cv2.imencode('.jpg', frame)
#             frame = buffer.tobytes()
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')        
                    
                    
                    
                    
                    
#                     # def check_face(self):
#                     #     results_mine = face_recognition.compare_faces([self.reference_encoding_mine], face_encoding)
#                     #     results_friend = face_recognition.compare_faces([self.reference_encoding_friend], face_encoding)

#             #             if any(results_mine):
#             #                 self.name = "Oqiljon Islomov"
#             #                 self.attendance("Oqiljon Islomov")
#             #             elif any(results_friend):
#             #                 self.name = "Saidvali Bahriddinov"
#             #                 self.attendance("Saidvali Bahriddinov")
#             #             else:
#             #                 self.name = "Topilmadi..."
#             #                 # self.attendance("Topilmadi...")

#             #             text_position = (x + 10, y + 280)
#             #             cv2.putText(frame, self.name, text_position, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

#             # ret, buffer = cv2.imencode('.jpg', frame)
#             # frame = buffer.tobytes()
#             # yield (b'--frame\r\n'
#             #        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')







import os
import cv2
import dlib
import face_recognition
from datetime import date
from .models import Students , Attendence , Groups
# pwd = os.path.dirname(__file__)


# def auto_attendence():
#     all_users=Students.objects.values('id')
#     print(all_users)
#     ids_list = [item['id'] for item in all_users]
#     print(f'id list: {ids_list}')
#     for user_id in ids_list:
#         user=Students.objects.get(pk=user_id)
#         att_user=Attendence.objects.filter(user_id=user).last()
#         if att_user is None :
#             try:
#                 Attendence.objects.create(user_id=user,date=date.today(),status=False)
#                 print('Attendance added for', user.username)
#             except Exception as e:
#                 print('func 1: Error adding attendance:', str(e))
        
#         elif att_user.date!=date.today() and att_user is not None:
#             try:
#                 Attendence.objects.create(user_id=user,date=date.today(),status=False)
#                 print('Attendance added for', user.username)
#             except Exception as e:
#                 print('func 2: Error adding attendance:', str(e))
#         else:
#             print('User', user.username, ' already axist !')


# class VideoCamera:
#     def __init__(self):
#         self.detector = dlib.get_frontal_face_detector()
#         self.cap = cv2.VideoCapture(0)
#         self.generate_frames_and_check_faces()
        
#     def attendance(self , name):
#         auto_attendence()
#         user = Students.objects.filter(username=name).first()
#         # att_user=Attendance.objects.filter(user_id=user).last()
#         ids=user.id if user else print("user yo'q")
#         users=Attendence.objects.filter(user_id=ids).last()
#         if users:
#             if ids is not None and users.status==False:
#                 try:
#                     users.status=True
#                     users.save()
#                     print('Attendance added for', name)
#                 except Exception as e:
#                     print('class ichi : Error adding attendance:', str(e))
#             else:
#                 print('User', name, 'is already in the database')

            
#     # def check_liveness(self, frame, face):
#     #     # Extract face region
#     #     x, y, w, h = face.left(), face.top(), face.width(), face.height()
#     #     face_region = frame[y:y+h, x:x+w]

#     #     # Convert face region to grayscale for motion analysis
#     #     if face_region is not None:
#     #         face_gray = cv2.cvtColor(face_region, cv2.COLOR_BGR2GRAY)

#     #         # Perform motion analysis (simple motion thresholding)
#     #         _, motion = cv2.threshold(face_gray, 30, 255, cv2.THRESH_BINARY)
#     #         motion_count = cv2.countNonZero(motion)
            
#     #         # If there's significant motion in the face region, consider it as live
#     #         return motion_count > 100  # Adjust threshold as needed
        
#     #     else:
#     #         print("Error: Face region is empty or invalid.")
#     #         pass
    
#     def check_liveness(self, frame, face):
#         # Extract face region
#         x, y, w, h = face.left(), face.top(), face.width(), face.height()
#         face_region = frame[y:y+h, x:x+w]

#         # Convert face region to grayscale for motion analysis
#         if face_region is not None:
#             face_gray = cv2.cvtColor(face_region, cv2.COLOR_BGR2GRAY)

#             # Perform motion analysis (simple motion thresholding)
#             _, motion = cv2.threshold(face_gray, 30, 255, cv2.THRESH_BINARY)
#             motion_count = cv2.countNonZero(motion)

#             # Calculate motion percentage relative to face region area
#             motion_percentage = (motion_count / (w * h)) * 100

#             # If motion percentage is below a certain threshold, consider it as live
#             return motion_percentage < 10
#         else:
#             print("Error: Face region is empty or invalid.")
#             return False

        
        
            
#     def generate_frames_and_check_faces(self):
#         while True:
#             ret, frame = self.cap.read()
#             if not ret:
#                 break

#             gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#             faces = self.detector(gray)

#             for face in faces:
#                 x, y, w, h = face.left(), face.top(), face.width(), face.height()
#                 center = (x + w // 2, y + h // 2)
#                 radius = int((w + h) // 3)
#                 cv2.circle(frame, center, radius, (0, 255, 0), 2)
                
#                  # Check liveness
#                 if self.check_liveness(frame, face):
#                     # If liveness check passes, perform face recognition

#                     face_locations = [(y, x + w, y + h, x)]
#                     face_encodings = face_recognition.face_encodings(frame, face_locations)
#                     # print(face_encodings)
#                     print('sooooooonnnnnnnnnnnnnnnnnnnnnnnnnnnn')

#                     if len(face_encodings) > 0:
#                         face_encoding = face_encodings[0]
#                         # media\images\Oqiljon_Islomov.JPG
#                         students=Students.objects.all()
#                         for item in students:  #(item["username"], item["image"]) 
#                             print('*******************************************')
#                             print(item.image)
#                             print(item.username)
#                             # print(item["image"])
#                             # print(item["username"])
#                             print(f'media/{item.image}')
#                             print('*******************************************')
#                             self.reference_image_path=f'media/{item.image}'
#                             self.reference_image = cv2.imread(self.reference_image_path)
#                             # self.reference_image = cv2.imread(item.image)
#                             self.reference_encoding = face_recognition.face_encodings(self.reference_image)[0]
#                             usernames=item.username
                            
#                             results_user = face_recognition.compare_faces([self.reference_encoding], face_encoding)
#                             print(results_user[0])
#                             print('8888888888888888888888888888888888888888888888888888888')

#                             if results_user[0]==True:
#                                 self.name = usernames
#                                 self.attendance(usernames)
                                
#                                 # text_position = (x + 10, y + 280)
#                                 # cv2.putText(frame, self.name, text_position, cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)
                                
#                             else:
#                                 self.name = "Topilmadi..."
                        
#                                 # text_position = (x + 10, y + 280)
#                                 # cv2.putText(frame, self.name, text_position, cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)
#                             text_position = (x + 10, y + 280)
#                             cv2.putText(frame, self.name, text_position, cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)
#             ret, buffer = cv2.imencode('.jpg', frame)
#             frame = buffer.tobytes()
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') 
            


            
def auto_attendance():
    all_users = Students.objects.values('id')
    ids_list = [item['id'] for item in all_users]
    for user_id in ids_list:
        user = Students.objects.get(pk=user_id)
        att_user = Attendence.objects.filter(user_id=user).last()
        if att_user is None:
            try:
                Attendence.objects.create(user_id=user, date=date.today(), status=False)
                print('Attendance added for', user.username)
            except Exception as e:
                print('func 1: Error adding attendance:', str(e))
        elif att_user.date != date.today() and att_user is not None:
            try:
                Attendence.objects.create(user_id=user, date=date.today(), status=False)
                print('Attendance added for', user.username)
            except Exception as e:
                print('func 2: Error adding attendance:', str(e))
        else:
            print('User', user.username, ' already exists!')

class VideoCamera:
    def __init__(self):
        self.detector = dlib.get_frontal_face_detector() # type: ignore
        self.cap = cv2.VideoCapture(1)
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml') # type: ignore
        self.generate_frames_and_check_faces()
        # face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        # eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        self.cwd = os.getcwd()
        
        self.dat_path="face_recog_app/shape_predictor_68_face_landmarks.dat"
        
        self.full_dat_path = os.path.join(cwd, dat_path)
        self.predictor = dlib.shape_predictor(full_dat_path)
        # self.pwd = os.path.dirname(__file__)
        # self.dat_path2="C:\Users\oqilj\OneDrive\Desktop\Intalim Face detect\face recog 2\face_recog\face_recog_app\shape_predictor_68_face_landmarks.dat"
        # self.predictor = dlib.shape_predictor(pwd+dat_path)
        self.EYE_AR_THRESH = 0.2
        self.EYE_AR_CONSEC_FRAMES = 3

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
                shape = predictor(gray, face)
                shape = shape_to_np(shape)

                # Extract the left and right eye coordinates
                left_eye = shape[l_start:l_end]
                right_eye = shape[r_start:r_end]

                # Calculate eye aspect ratio for each eye
                left_ear = eye_aspect_ratio(left_eye)
                right_ear = eye_aspect_ratio(right_eye)

                # Average the eye aspect ratio for both eyes
                ear = (left_ear + right_ear) / 2.0

                # Draw the eyes region
                left_eye_hull = cv2.convexHull(left_eye)
                right_eye_hull = cv2.convexHull(right_eye)
                cv2.drawContours(frame, [left_eye_hull], -1, (0, 255, 0), 1)
                cv2.drawContours(frame, [right_eye_hull], -1, (0, 255, 0), 1)

                # Check if the eye aspect ratio is below the threshold
                if ear < EYE_AR_THRESH:
                    COUNTER += 1
                else:
                    if COUNTER >= EYE_AR_CONSEC_FRAMES:
                        TOTAL += 1
                    COUNTER = 0
                
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
                            if results_user[0] == True:
                                self.name = usernames
                                self.attendance(usernames)
                            else:
                                self.name = "Not found"

                            text_position = (x + 10, y + 280)
                            cv2.putText(frame, self.name, text_position, cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)

            # Display the total number of blinks
            cv2.putText(frame, f"Blinks: {TOTAL}", (10, 60),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

            # Display the frame
            cv2.imshow("Frame", frame)
            
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
