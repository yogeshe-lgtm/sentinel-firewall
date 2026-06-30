"""
Sentinel Firewall
SQLite Database Module
"""

import sqlite3

DATABASE = "database/firewall.db"


def initialize_database():
    """
    Create the database and events table.
    """

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,

            source_ip TEXT,

            destination_ip TEXT,

            protocol TEXT,

            destination_port INTEGER,

            action TEXT,

            threat TEXT

        )
    """)

    connection.commit()

    connection.close()


def insert_event(source,
                 destination,
                 protocol,
                 port,
                 action,
                 threat):

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO events
        (
            source_ip,
            destination_ip,
            protocol,
            destination_port,
            action,
            threat
        )
        VALUES
        (?, ?, ?, ?, ?, ?)
        """,
        (
            source,
            destination,
            protocol,
            port,
            action,
            threat
        )
    )

    connection.commit()

    connection.close()
