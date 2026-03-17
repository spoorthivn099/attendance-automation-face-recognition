# Attendance Automation System with Face Recognition

A smart attendance management system using Face Recognition, Python, MySQL, and Flask.

## 🚀 Features
- Face recognition based attendance marking
- Automatic Punch IN and Punch OUT
- Web dashboard with date filtering
- Excel report generation
- Auto scheduler for daily reports
- MySQL database storage

## 🛠️ Technologies Used
- **Python 3.13** — Core programming language
- **OpenCV** — Camera and video processing
- **DeepFace** — Face recognition AI model
- **MySQL** — Database storage
- **Flask** — Web dashboard
- **Pandas / OpenPyXL** — Excel report generation


## 📁 Project Structure
```
attendance_dashboard/
├── main.py                  # Master control menu
├── attendance_system.py     # Face recognition system
├── enroll_employee.py       # Employee enrollment
├── generate_report.py       # Excel report generator
├── scheduler.py             # Auto daily scheduler
├── app.py                   # Flask web server
├── send_alerts.py           # Email alerts
└── templates/
        └── dashboard.html   # Web dashboard
```

## ⚙️ Installation

### Step 1: Install Python 3.13
Download from python.org/downloads

### Step 2: Install required libraries
```
pip install opencv-python
pip install deepface
pip install tf-keras
pip install tensorflow
pip install mysql-connector-python
pip install numpy pandas flask openpyxl schedule
```

### Step 3: Setup MySQL Database
- Install MySQL Community Edition
- Open MySQL Workbench
- Run this SQL:
```sql
CREATE DATABASE attendance_db;
USE attendance_db;

CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    email VARCHAR(100),
    face_embedding LONGTEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    date DATE,
    punch_in TIME,
    punch_out TIME,
    status VARCHAR(50),
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);
```

### Step 4: Update database password
Open each Python file and update:
```python
password="your_mysql_password"
```

## 🚀 How to Run

### Start the complete system:
```
python main.py
```

### Menu Options:
| Option | Action |
|--------|--------|
| 1 | Start Attendance System |
| 2 | Enroll New Employee |
| 3 | Generate Excel Report |
| 4 | Start Auto Scheduler |
| 5 | Open Web Dashboard |
| 6 | Exit |

## 👤 How to Enroll Employees
1. Run `python main.py`
2. Press **2** to enroll
3. Enter name, department, email
4. Look at camera
5. Press **SPACEBAR** to capture face

## 📋 How to Mark Attendance
1. Run `python main.py`
2. Press **1** to start attendance system
3. Look at camera — your name appears in green
4. Press **I** to Punch IN
5. Press **O** to Punch OUT
6. Press **Q** to quit

## 📊 How to View Dashboard
1. Run `python main.py`
2. Press **5** to open dashboard
3. Browser opens at http://127.0.0.1:5000
4. Use date filter to view any day's attendance

## 📈 How to Generate Excel Report
1. Run `python main.py`
2. Press **3** to generate report
3. Excel file saved in project folder

## 🗄️ Database Structure

### Employees Table
| Column | Type | Description |
|--------|------|-------------|
| id | INT | Employee ID |
| name | VARCHAR | Employee name |
| department | VARCHAR | Department |
| email | VARCHAR | Email address |
| face_embedding | LONGTEXT | Face data |
| created_at | TIMESTAMP | Registration date |

### Attendance Table
| Column | Type | Description |
|--------|------|-------------|
| id | INT | Record ID |
| employee_id | INT | Employee reference |
| date | DATE | Attendance date |
| punch_in | TIME | Punch in time |
| punch_out | TIME | Punch out time |
| status | VARCHAR | Present/Absent |

## 👨‍💻 Developer
- Built with Python, MySQL, DeepFace, Flask
- Face Recognition using FaceNet model
- Web Dashboard using Flask + HTML/CSS

## 📝 Notes
- Make sure camera is connected before running
- First run downloads AI models (takes 2-3 minutes)
- Punch OUT only available after 4 hours of Punch IN
- Dashboard auto refreshes every 10 seconds
```

Save with **Ctrl+S**!

---

Your project folder should now look like this:
```
attendence_dashboard/
├── main.py
├── attendance_system.py
├── enroll_employee.py
├── generate_report.py
├── scheduler.py
├── app.py
├── send_alerts.py
├── README.md          ← new!
└── templates/
        └── dashboard.html