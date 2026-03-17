import schedule
import time
import subprocess
import os
from datetime import datetime

print("✅ Attendance Automation Scheduler Started!")
print("Running automatically every day...")
print("Press Ctrl+C to stop\n")

def run_report():
    print(f"\n⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Generating Excel report...")
    try:
        subprocess.run(['python', 'generate_report.py'], check=True)
        print("✅ Excel report generated!")
    except Exception as e:
        print(f"❌ Report error: {e}")

def run_attendance_summary():
    print(f"\n⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Running daily summary...")
    try:
        import mysql.connector
        from datetime import date

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Anu@2005",
            database="attendance_db"
        )
        cursor = conn.cursor()
        today = date.today()

        cursor.execute("""
            SELECT e.name, e.department, a.punch_in, a.punch_out, a.status
            FROM attendance a
            JOIN employees e ON a.employee_id = e.id
            WHERE a.date=%s
        """, (today,))
        present = cursor.fetchall()

        cursor.execute("""
            SELECT e.name, e.department
            FROM employees e
            WHERE e.id NOT IN (
                SELECT employee_id FROM attendance WHERE date=%s
            )
        """, (today,))
        absent = cursor.fetchall()
        conn.close()

        print(f"\n📊 Daily Summary for {today}")
        print(f"{'='*40}")
        print(f"✅ Present: {len(present)}")
        for emp in present:
            print(f"   - {emp[0]} ({emp[1]}) | IN: {emp[2]} | OUT: {emp[3] if emp[3] else 'Not yet'}")

        print(f"\n❌ Absent: {len(absent)}")
        for emp in absent:
            print(f"   - {emp[0]} ({emp[1]})")
        print(f"{'='*40}\n")

    except Exception as e:
        print(f"❌ Summary error: {e}")

# ── Schedule tasks ──
# Generate report at 6:00 PM every day
schedule.every().day.at("18:00").do(run_report)

# Print summary at 9:00 AM every day
schedule.every().day.at("09:00").do(run_attendance_summary)

# Also run every hour to check
schedule.every(1).hours.do(run_attendance_summary)

# Run once immediately when started
run_attendance_summary()

print("📅 Scheduled tasks:")
print("   - 09:00 AM → Daily attendance summary")
print("   - 06:00 PM → Generate Excel report")
print("   - Every 1 hour → Attendance check\n")

while True:
    schedule.run_pending()
    time.sleep(60)
