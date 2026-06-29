import sqlite3
 
def save_data(cpu, memory, disk):
    conn = sqlite3.connect("health_monitor.db")
    cursor = conn.cursor()
 
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS system_health (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        cpu REAL,
        memory REAL,
        disk REAL
    )
    """)
 
    cursor.execute(
        "INSERT INTO system_health (cpu, memory, disk) VALUES (?, ?, ?)",
        (cpu, memory, disk)
    )
 
    conn.commit()
    conn.close()