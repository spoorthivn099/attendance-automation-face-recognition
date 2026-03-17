from flask import Flask, render_template, jsonify, request
import mysql.connector
from datetime import date

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Anu@2005",
        database="attendance_db"
    )

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/attendance')
def get_attendance():
    filter_date = request.args.get('date', str(date.today()))
    
    conn = get_db()
    cursor = conn.cursor()
    
    if filter_date == 'all':
        cursor.execute("""
            SELECT e.name, e.department, a.date,
                   a.punch_in, a.punch_out, a.status
            FROM attendance a
            JOIN employees e ON a.employee_id = e.id
            ORDER BY a.date DESC, a.punch_in DESC
        """)
    else:
        cursor.execute("""
            SELECT e.name, e.department, a.date,
                   a.punch_in, a.punch_out, a.status
            FROM attendance a
            JOIN employees e ON a.employee_id = e.id
            WHERE a.date = %s
            ORDER BY a.punch_in DESC
        """, (filter_date,))
    
    rows = cursor.fetchall()
    conn.close()

    data = []
    for row in rows:
        data.append({
            "name": row[0],
            "department": row[1],
            "date": str(row[2]),
            "punch_in": str(row[3]) if row[3] else "-",
            "punch_out": str(row[4]) if row[4] else "-",
            "status": row[5]
        })
    return jsonify(data)

@app.route('/api/summary')
def get_summary():
    filter_date = request.args.get('date', str(date.today()))
    
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM employees")
    total = cursor.fetchone()[0]

    if filter_date == 'all':
        cursor.execute("SELECT COUNT(DISTINCT employee_id) FROM attendance")
    else:
        cursor.execute(
            "SELECT COUNT(*) FROM attendance WHERE date=%s",
            (filter_date,)
        )
    present = cursor.fetchone()[0]
    absent = total - present
    conn.close()

    return jsonify({
        "total": total,
        "present": present,
        "absent": absent,
        "date": filter_date
    })

if __name__ == '__main__':
    app.run(debug=True)