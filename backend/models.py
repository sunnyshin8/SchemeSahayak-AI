from datetime import datetime
from pydantic import BaseModel
import sqlite3
import json

DB_NAME = "audit.db"

class AuditLogEntry(BaseModel):
    timestamp: str
    agency_id: str = "SYSTEM" # Default or from auth
    action: str
    details: str

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS audit_logs
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  timestamp TEXT, 
                  agency_id TEXT, 
                  action TEXT, 
                  details TEXT)''')
    conn.commit()
    conn.close()

def log_audit(action: str, details: dict, agency_id: str = "SYSTEM"):
    try:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        dt_string = datetime.now().isoformat()
        details_str = json.dumps(details)
        c.execute("INSERT INTO audit_logs (timestamp, agency_id, action, details) VALUES (?, ?, ?, ?)",
                  (dt_string, agency_id, action, details_str))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Audit Log Failed: {e}")
