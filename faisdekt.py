import face_recognition
import cv2
import numpy as np

# ১. পরিচিত মুখ লোড করা
image_1 = face_recognition.load_image_file("mursalin.jpg")
encoding_1 = face_recognition.face_encodings(image_1)[0]

known_face_encodings = [encoding_1]
known_face_names = ["Mursalin"]

# ২. ক্যামেরা চালু করা
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    # বর্তমান ফ্রেমের মুখ চেনা
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # নামের বক্স তৈরি করা
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()