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
def auto_attendence():
    all_users=Users.objects.values('id')
    print(all_users)
    ids_list = [item['id'] for item in all_users]
    print(ids_list)
    for user_id in ids_list:
        user=Users.objects.get(pk=user_id)
        att_user=Attendance.objects.filter(user_id=user_id).last()
        if att_user.date!=date.today():
            try:
                Attendance.objects.create(user_id=user_id,date=date.today(),status=False)
                print('Attendance added for', user.username)
            except Exception as e:
                print('Error adding attendance:', str(e))
        else:
            print('User', user.username, ' already axist !')






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








import cv2
import dlib
import face_recognition
from datetime import date
from .models import Students , Attendence , Groups


def auto_attendence():
    all_users=Students.objects.values('id')
    print(all_users)
    ids_list = [item['id'] for item in all_users]
    print(ids_list)
    for user_id in ids_list:
        user=Students.objects.get(pk=user_id)
        att_user=Attendence.objects.filter(user_id=user_id).last()
        if att_user is None :
            try:
                Attendence.objects.create(user_id=user_id,date=date.today(),status=False)
                print('Attendance added for', user.username)
            except Exception as e:
                print('Error adding attendance:', str(e))
        
        elif att_user.date!=date.today() and att_user is not None:
            try:
                Attendence.objects.create(user_id=user_id,date=date.today(),status=False)
                print('Attendance added for', user.username)
            except Exception as e:
                print('Error adding attendance:', str(e))
        else:
            print('User', user.username, ' already axist !')





class VideoCamera:
    def __init__(self):
        self.detector = dlib.get_frontal_face_detector()
        self.cap = cv2.VideoCapture(0)
        self.generate_frames_and_check_faces()
        
    def attendance(self , name):
        auto_attendence()
        user = Students.objects.filter(username=name).first()
        # att_user=Attendance.objects.filter(user_id=user).last()
        ids=user.id if user else print("user yo'q")
        users=Attendence.objects.filter(user_id=ids).last()
        if ids is not None and users.status==False:
            try:
                users.status=True
                users.save()
                print('Attendance added for', name)
            except Exception as e:
                print('Error adding attendance:', str(e))
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

                face_locations = [(y, x + w, y + h, x)]
                face_encodings = face_recognition.face_encodings(frame, face_locations)

                if len(face_encodings) > 0:
                    face_encoding = face_encodings[0]
                    # media\images\Oqiljon_Islomov.JPG
                    students=Students.objects.all()
                    for item in students:  #(item["username"], item["image"]) 
                        print('*******************************************')
                        print(item.image)
                        print(item.username)
                        # print(item["image"])
                        # print(item["username"])
                        print(f'media/{item.image}')
                        print('*******************************************')
                        self.reference_image_path=f'media/{item.image}'
                        self.reference_image = cv2.imread(self.reference_image_path)
                        # self.reference_image = cv2.imread(item.image)
                        self.reference_encoding = face_recognition.face_encodings(self.reference_image)[0]
                        usernames=item.username
                        
                        results_mine = face_recognition.compare_faces([self.reference_encoding], face_encoding)

                        if any(results_mine):
                            self.name = usernames
                            self.attendance(usernames)
                        else:
                            self.name = "Topilmadi..."
                    
                        text_position = (x + 10, y + 280)
                        cv2.putText(frame, self.name, text_position, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') 