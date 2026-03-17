from deepface import DeepFace
import cv2

cap = cv2.VideoCapture(0)
print("Looking for face... Press Q to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    try:
        result = DeepFace.analyze(frame, actions=['age', 'gender'], enforce_detection=False)
        age = result[0]['age']
        gender = result[0]['dominant_gender']
        
        cv2.putText(frame, f"Age: {age}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, f"Gender: {gender}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    except:
        pass

    cv2.imshow("DeepFace Test", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
