import cv2
import mysql.connector
from deepface import DeepFace
import json
import numpy as np
from datetime import datetime, date

# Connect to database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Anu@2005",
    database="attendance_db"
)
cursor = conn.cursor()

# Load all employee face embeddings from database
print("Loading employee faces from database...")
cursor.execute("SELECT id, name, face_embedding FROM employees WHERE face_embedding IS NOT NULL")
employees = cursor.fetchall()

employee_data = []
for emp in employees:
    emp_id, name, embedding_json = emp
    embedding = json.loads(embedding_json)
    employee_data.append({
        "id": emp_id,
        "name": name,
        "embedding": embedding
    })

print(f"Loaded {len(employee_data)} employees!")
print("Controls: I = Punch IN | O = Punch OUT | Q = Quit")

def punch_in(employee_id, name):
    today = date.today()
    now = datetime.now().strftime("%H:%M:%S")

    cursor.execute(
        "SELECT id, punch_in FROM attendance WHERE employee_id=%s AND date=%s",
        (employee_id, today)
    )
    record = cursor.fetchone()

    if record is None:
        cursor.execute(
            "INSERT INTO attendance (employee_id, date, punch_in, status) VALUES (%s, %s, %s, %s)",
            (employee_id, today, now, "Present")
        )
        conn.commit()
        print(f"✅ {name} punched IN at {now}")
        return f"✓ PUNCH IN: {name} at {now}", (0, 255, 0)
    else:
        print(f"⚠️ {name} already punched IN today!")
        return f"⚠ Already punched IN today!", (0, 165, 255)

def punch_out(employee_id, name):
    today = date.today()
    now = datetime.now().strftime("%H:%M:%S")

    cursor.execute(
        "SELECT id, punch_in, punch_out FROM attendance WHERE employee_id=%s AND date=%s",
        (employee_id, today)
    )
    record = cursor.fetchone()

    if record is None:
        print(f"⚠️ {name} has not punched IN yet!")
        return f"⚠ Please punch IN first!", (0, 0, 255)

    elif record[2] is None:
        cursor.execute(
            "UPDATE attendance SET punch_out=%s WHERE employee_id=%s AND date=%s",
            (now, employee_id, today)
        )
        conn.commit()
        print(f"✅ {name} punched OUT at {now}")
        return f"✓ PUNCH OUT: {name} at {now}", (255, 0, 0)

    else:
        print(f"⚠️ {name} already punched OUT today!")
        return f"⚠ Already punched OUT today!", (0, 165, 255)

# Start camera
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

current_name = "Unknown"
current_id = None
status_text = "Look at camera"
status_color = (255, 255, 255)
recognized = False

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    # Recognize face every frame
    try:
        detected = DeepFace.represent(frame,
                                      model_name="Facenet",
                                      enforce_detection=False)

        if detected and detected[0]:
            current_embedding = detected[0]['embedding']
            best_match = None
            best_distance = 999

            for emp in employee_data:
                stored = np.array(emp['embedding'])
                current = np.array(current_embedding)
                distance = np.linalg.norm(stored - current)

                if distance < best_distance:
                    best_distance = distance
                    best_match = emp

            if best_match and best_distance < 10:
                current_name = best_match['name']
                current_id = best_match['id']
                recognized = True
            else:
                current_name = "Unknown Person"
                current_id = None
                recognized = False

    except Exception as e:
        pass

    # Draw UI on frame
    # Top bar background
    cv2.rectangle(frame, (0, 0), (frame.shape[1], 50), (0, 0, 0), -1)

    # Date and time
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cv2.putText(frame, now_str, (10, 35),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    # Bottom bar background
    cv2.rectangle(frame, (0, frame.shape[0]-120),
                  (frame.shape[1], frame.shape[0]), (0, 0, 0), -1)

    # Show recognized name
    if recognized:
        cv2.putText(frame, f"Face: {current_name}", (20, frame.shape[0]-85),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    else:
        cv2.putText(frame, f"Face: {current_name}", (20, frame.shape[0]-85),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # Show controls
    cv2.putText(frame, "Press I = Punch IN   |   O = Punch OUT   |   Q = Quit",
                (20, frame.shape[0]-55),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 1)

    # Show status
    cv2.putText(frame, status_text, (20, frame.shape[0]-20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, status_color, 2)

    cv2.imshow("Attendance System", frame)

    key = cv2.waitKey(1) & 0xFF

    # Press I for Punch IN
    if key == ord('i'):
        if recognized and current_id:
            status_text, status_color = punch_in(current_id, current_name)
        else:
            status_text = "⚠ No face recognized! Look at camera"
            status_color = (0, 0, 255)

    # Press O for Punch OUT
    elif key == ord('o'):
        if recognized and current_id:
            status_text, status_color = punch_out(current_id, current_name)
        else:
            status_text = "⚠ No face recognized! Look at camera"
            status_color = (0, 0, 255)

    # Press Q to quit
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
conn.close()
print("Attendance system closed!")