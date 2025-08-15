
import os
import json
import shutil
import sqlite3
from datetime import datetime

def reserve_vacation_time(employee_id, start_date, end_date):
    conn = sqlite3.connect('/tmp/employee_database.db')
    c = conn.cursor()
    
    if not employee_id:
        conn.close()
        raise Exception("No employee id provided")
    
    if not start_date or not end_date:
        conn.close()
        raise Exception("Both start_date and end_date are required")
    
    try:
        # Calculate vacation days requested
        start_date_obj = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date_obj = datetime.strptime(end_date, '%Y-%m-%d').date()
        vacation_days_requested = (end_date_obj - start_date_obj).days + 1
        
        current_year = datetime.now().year
        
        # Insert the planned vacation
        c.execute("""
            INSERT INTO planned_vacations 
            (employee_id, vacation_start_date, vacation_end_date, vacation_days_taken) 
            VALUES (?, ?, ?, ?)
        """, (employee_id, start_date, end_date, vacation_days_requested))
        
        # Update vacation days
        c.execute("""
            UPDATE vacations 
            SET employee_vacation_days_taken = employee_vacation_days_taken + ?, 
                employee_vacation_days_available = employee_vacation_days_available - ?
            WHERE employee_id = ? AND year = ?
        """, (vacation_days_requested, vacation_days_requested, employee_id, current_year))
        
        conn.commit()
        conn.close()
        
        return f"Vacation reserved successfully from {start_date} to {end_date} ({vacation_days_requested} days)"
        
    except Exception as e:
        conn.rollback()
        conn.close()
        raise Exception(str(e))
