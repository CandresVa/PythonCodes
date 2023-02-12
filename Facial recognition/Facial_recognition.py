import cv2
import face_recognition as fr

#Load pictures
photo_control = fr.load_image_file('FotoA.jpg')
photo_test = fr.load_image_file('FotoB.jpg')

#Move pictures to RGB
photo_control = cv2.cvtColor(photo_control, cv2.COLOR_BGR2RGB)
photo_test = cv2.cvtColor(photo_test, cv2.COLOR_BGR2RGB)

#Locate control face
Locate_face_A = fr.face_locations(photo_control)[0]
face_codify_A = fr.face_encodings(photo_control)[0]

print(locate_face_A)

#Locate test face
Locate_face_B = fr.face_locations(photo_test)[0]
face_codify_B = fr.face_encodings(photo_test)[0]

print(locate_face_A)

#Show rectangle
cv2.rectangle(photo_control,
              (locate_face_A[3],locate_face_A[0]),
              (locate_face_A[1], locate_face_A[2]),
              (0, 255, 0),
              2)
cv2.rectangle(photo_test,
              (locate_face_B[3],locate_face_B[0]),
              (locate_face_B[1], locate_face_B[2]),
              (0, 255, 0),
              2)
#Comparison
result = fr.compare_faces([face_codify_A], face_codify_B)
print(result)
#The result is possible beacause if arroud less 0.6 of match
#Tou can modify the value:
#result = fr.compare_faces([face_codify_A], face_codify_B,0.3)
#Now the comparison value is 0.3

#Distance meassure
distance = fr. face_distance([face_codify_A], face_codify_B)
print(distance)

#Show results:
cv2.putText(photo_test,
            f'{result} {distance.round(2)}',
            (50,50),
            cv2.FONT_HERSEY_COMPLEX,
            1,
            (0,255,0),
            2)

#Show pictures
cv2.imshow('Photo control', photo_control)
cv2.imshow('Photo test', photo_test)

#Keep the program runing
cv2.waikey(0)