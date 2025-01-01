import cv2
import face_recognition
from datetime import datetime as dt
import attendence
import json
import dlib

print(dlib.DLIB_USE_CUDA)


known_face_encodings = []
known_face_names = ["Sameer","Karthik","Krutik","Lydia","Shivanshu","Anmol"]

known_person1_img = face_recognition.load_image_file("faces/sam.jpg")
known_person2_img = face_recognition.load_image_file("faces/karthik.jpg")
known_person3_img = face_recognition.load_image_file("faces/krutik.jpg")
known_person4_img = face_recognition.load_image_file("faces/lydia.png")
known_person5_img = face_recognition.load_image_file("faces/shivanshu.png")
known_person6_img = face_recognition.load_image_file("faces/anmol.jpg")

known_person1_encoding = face_recognition.face_encodings(known_person1_img)[0]
known_person2_encoding = face_recognition.face_encodings(known_person2_img)[0]
known_person3_encoding = face_recognition.face_encodings(known_person3_img)[0]
known_person4_encoding = face_recognition.face_encodings(known_person4_img)[0]
known_person5_encoding = face_recognition.face_encodings(known_person5_img)[0]
known_person6_encoding = face_recognition.face_encodings(known_person6_img)[0]

known_face_encodings.append(known_person1_encoding)
known_face_encodings.append(known_person2_encoding)
known_face_encodings.append(known_person3_encoding)
known_face_encodings.append(known_person4_encoding)
known_face_encodings.append(known_person5_encoding)
known_face_encodings.append(known_person6_encoding)

checkvalue = []

with open("Rollcalls.txt") as file:
    data = file.read()

js = json.loads(data)

########

video = cv2.VideoCapture(0)

a = 3 
while True:
    
    ret, frame = video.read()
    
    face_locations = face_recognition.face_locations(img=frame, model="cnn")
    face_encodings = face_recognition.face_encodings(frame, face_locations, num_jitters=50)
    
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.4)
        name = "unknown"

        
        

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            
            
            roll = js[name]
            for i in range(0,11):
                if name not in checkvalue:
                    matchtxt = cv2.putText(frame, "Attedance Taken", (10,30), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,225), 2)
                    currtime = dt.now()
                    curtime = f"{currtime.hour} : {currtime.minute} : {currtime.second}"
                    curdate = f"{currtime.day}/{currtime.month}/{currtime.year}"
                    attendence.present(roll,name,a,curdate,curtime)
                    a+=1      
                    checkvalue.append(name)
                

        cv2.rectangle(frame, (left, top), (right, bottom), (0,0,225), 2)
        cv2.putText(frame, name, (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,225), 2)
        

    
    cv2.imshow("Frame", frame)
    k = cv2.waitKey(20)
    if k & 0xFF == ord('q'):
        break



video.release()
cv2.destroyAllWindows()

