import subprocess
import sys
import os
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    clear_screen()
    print("="*50)
    print("   ATTENDANCE AUTOMATION SYSTEM")
    print(f"   {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*50)
    print("\n  1. Start Attendance System (Face Recognition)")
    print("  2. Enroll New Employee")
    print("  3. Generate Excel Report")
    print("  4. Start Auto Scheduler")
    print("  5. Open Dashboard (Web)")
    print("  6. Exit")
    print("\n" + "="*50)

while True:
    print_menu()
    choice = input("\n  Enter your choice (1-6): ")

    if choice == '1':
        print("\n✅ Starting Attendance System...")
        print("Press Q in camera window to stop\n")
        subprocess.run(['python', 'attendance_system.py'])

    elif choice == '2':
        print("\n✅ Opening Enrollment System...")
        subprocess.run(['python', 'enroll_employee.py'])

    elif choice == '3':
        print("\n✅ Generating Excel Report...")
        subprocess.run(['python', 'generate_report.py'])
        print("\nReport saved in your project folder!")
        input("\nPress Enter to continue...")

    elif choice == '4':
        print("\n✅ Starting Auto Scheduler...")
        print("Press Ctrl+C to stop\n")
        subprocess.run(['python', 'scheduler.py'])

    elif choice == '5':
        print("\n✅ Starting Dashboard...")
        print("Opening http://127.0.0.1:5000 in browser\n")
        import webbrowser
        import threading
        def open_browser():
            import time
            time.sleep(2)
            webbrowser.open('http://127.0.0.1:5000')
        threading.Thread(target=open_browser).start()
        subprocess.run(['python', 'app.py'])

    elif choice == '6':
        print("\n👋 Goodbye!")
        sys.exit()

    else:
        print("\n❌ Invalid choice! Please enter 1-6")
        input("Press Enter to continue...")
