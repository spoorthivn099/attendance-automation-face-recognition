# Automated Attendance System Using Face Recognition

A smart attendance management system built using Face Recognition, Python, MySQL and Flask.

## 👩‍💻 Developer
- **Name:** Spoorthi V N
- **Department:** ECE
- **College:** PESITM, Shivamogga

## 🚀 Features
- Face recognition based attendance marking
- Automatic Punch IN and Punch OUT using keyboard
- Web dashboard with date filtering
- Excel report generation
- Auto scheduler for daily reports
- MySQL database storage
- Unknown face detection

## 🛠️ Technologies Used
- **Python 3.13** — Core programming language
- **OpenCV** — Camera and video processing
- **DeepFace** — Face recognition AI (FaceNet model)
- **MySQL** — Database storage
- **Flask** — Web dashboard
- **Pandas / OpenPyXL** — Excel report generation
- **Schedule** — Automatic task scheduling
- **CMake** — Required for face recognition libraries

## 📁 Project Structure
```
attendence_dashboard/
├── main.py                  # Master control menu
├── attendance_system.py     # Face recognition + Punch IN/OUT
├── enroll_employee.py       # Employee face enrollment
├── generate_report.py       # Excel report generator
├── scheduler.py             # Auto daily scheduler
├── app.py                   # Flask web server
├── README.md                # Project documentation
└── templates/
        └── dashboard.html   # Web dashboard UI
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
pip install numpy pandas flask openpyxl schedule cmake
```

### Step 3: Setup MySQL Database
- Install MySQL Community Edition
- Install MySQL Workbench
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
2. Press **2** to enroll new employee
3. Camera opens — press **SPACEBAR** to capture face
4. Enter name, department and email
5. Face is saved to database automatically

## 📋 How to Mark Attendance
1. Run `python main.py`
2. Press **1** to start attendance system
3. Look at camera — your name appears in green
4. Press **I** to Punch IN ✅
5. Press **O** to Punch OUT ✅
6. Press **Q** to quit

## 📊 How to View Dashboard
1. Run `python main.py`
2. Press **5** to open dashboard
3. Browser opens at http://127.0.0.1:5000
4. Use date filter to view any day's attendance
5. Click All Records to view complete history

## 📈 How to Generate Excel Report
1. Run `python main.py`
2. Press **3** to generate report
3. Excel file saved in project folder as
   `attendance_report_YYYY-MM-DD.xlsx`

## 🗄️ Database Structure

### Employees Table
| Column | Type | Description |
|--------|------|-------------|
| id | INT | Employee ID |
| name | VARCHAR | Employee name |
| department | VARCHAR | Department |
| email | VARCHAR | Email address |
| face_embedding | LONGTEXT | Face recognition data |
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

## 📝 Important Notes
- Make sure camera is connected before running
- First run downloads AI models (takes 2-3 minutes)
- Punch OUT only available after 4 hours of Punch IN
- Dashboard auto refreshes every 10 seconds
- Unknown faces are shown in red on camera

## 🎯 Future Enhancements
- Email alerts for absent employees
- UiPath RPA automation for HR reporting
- Mobile app integration
- Multiple camera support
