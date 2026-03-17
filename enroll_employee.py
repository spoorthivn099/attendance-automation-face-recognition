import cv2
import mysql.connector
from deepface import DeepFace
import json

# Step 1: Take photo first
print("Opening camera... Press SPACE to take photo, Q to quit")

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # CAP_DSHOW fixes Windows camera issues

saved_frame = None

while True:
    ret, frame = cap.read()
    if not ret:
        continue
    
    cv2.imshow("Press SPACE to capture", frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord(' '):  # spacebar
        saved_frame = frame.copy()
        print("Photo captured!")
        break
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

if saved_frame is None:
    print("No photo taken. Exiting.")
    exit()

# Step 2: Get employee details
name = input("Enter employee name: ")
department = input("Enter department: ")
email = input("Enter email: ")

# Step 3: Save to database
print("Processing face... please wait.")

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Anu@2005",
        database="attendance_db"
    )
    cursor = conn.cursor()
    embedding = DeepFace.represent(saved_frame, 
                                   model_name="Facenet",
                                   enforce_detection=False)
    embedding_json = json.dumps(embedding[0]['embedding'])

    cursor.execute(
        "INSERT INTO employees (name, department, email, face_embedding) VALUES (%s, %s, %s, %s)",
        (name, department, email, embedding_json)
    )
    conn.commit()
    print(f"Successfully enrolled {name}!")
    conn.close()

except Exception as e:
    print(f"Error: {e}")
