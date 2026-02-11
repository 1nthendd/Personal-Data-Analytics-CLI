"""
Database module for Personal Productivity Manager.
"""

import sqlite3


def connect_to_db():
    """Establish connection to SQLite database.
    """
    connection = sqlite3.connect('productivity.db')
    connection.row_factory = sqlite3.Row
    return connection


def create_table(conn):
    """Create productivity table if it doesn't exist.
    """
    request = """CREATE TABLE IF NOT EXISTS productivity (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    study_hours REAL NOT NULL CHECK(study_hours BETWEEN 0 AND 24),
    sport_hours REAL NOT NULL CHECK(sport_hours BETWEEN 0 AND 24),
    mood INTEGER NOT NULL CHECK(mood BETWEEN 1 AND 10),
    note TEXT);"""
    conn.execute(request)
    conn.commit()


def add_entry(conn, date, study_hours, sport_hours, mood, note):
    """Insert a new productivity entry into the database.
    
    Args:
        conn (sqlite3.Connection): Database connection object.
        date (str): Entry date in YYYY-MM-DD format.
        study_hours (float): Study hours (0-24).
        sport_hours (float): Sport hours (0-24).
        mood (int): Mood rating (1-10).
        note (str): Optional note about the day.
    """
    request = """INSERT INTO productivity(date, study_hours, sport_hours, mood, note)
    VALUES(?, ?, ?, ?, ?)"""
    conn.execute(request, (date, study_hours, sport_hours, mood, note))
    conn.commit()


def get_all_entries(conn):
    """Retrieve all productivity entries from the database.
    """
    request = "SELECT * FROM productivity"
    cursor = conn.cursor()
    cursor.execute(request)
    all_entries = cursor.fetchall()
    return all_entries


def delete_entry(conn, entry_id):
    """Delete a productivity entry by ID.
    """
    request = "DELETE FROM productivity WHERE id = ?"
    cursor = conn.cursor()
    cursor.execute(request, (entry_id,))
    conn.commit()
    rows = cursor.rowcount
    return rows


def update_entry(conn, entry_id, date, study_hours, sport_hours, mood, note):
    """Update an existing productivity entry.
    """
    cursor = conn.cursor()
    request = """UPDATE productivity
    SET date = ?,
    study_hours = ?,
    sport_hours = ?,
    mood = ?,
    note = ?
    WHERE id = ?"""
    cursor.execute(request, (date, study_hours, sport_hours, mood, note, entry_id))
    conn.commit()
    rows = cursor.rowcount
    return rows 