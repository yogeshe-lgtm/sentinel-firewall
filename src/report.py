"""
Sentinel Firewall Report Generator
"""

import sqlite3
import pandas as pd

DATABASE = "database/firewall.db"


def generate_report():

    connection = sqlite3.connect(DATABASE)

    query = """
        SELECT
            timestamp,
            source_ip,
            destination_ip,
            protocol,
            destination_port,
            action,
            threat
        FROM events
    """

    dataframe = pd.read_sql_query(query, connection)

    connection.close()

    dataframe.to_csv(
        "database/firewall_report.csv",
        index=False
    )

    print("\nReport generated successfully!")
    print("Saved to: database/firewall_report.csv")

def generate_summary():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM events")

    total = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM events WHERE action='BLOCK'"
    )

    blocked = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM events WHERE action='ALLOW'"
    )

    allowed = cursor.fetchone()[0]

    connection.close()

    print("\n========== Firewall Summary ==========")
    print(f"Total Events : {total}")
    print(f"Allowed      : {allowed}")
    print(f"Blocked      : {blocked}")
