import os
import sqlite3

DB_PATH = "/workspace/app.db"

def main() -> None:
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    connection = sqlite3.connect(DB_PATH)
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                col_left TEXT NOT NULL,
                col_right TEXT NOT NULL
            );
            """
        )
        connection.commit()

        cursor.execute("DELETE FROM items;")
        connection.commit()

        sample_rows = [
            ("Row 1", "Value 1"),
            ("Row 2", "Value 2"),
            ("Row 3", "Value 3"),
            ("Row 4", "Value 4"),
            ("Row 5", "Value 5"),
            ("Row 6", "Value 6"),
            ("Row 7", "Value 7"),
            ("Row 8", "Value 8"),
            ("Row 9", "Value 9"),
            ("Row 10", "Value 10"),
        ]

        cursor.executemany(
            "INSERT INTO items (col_left, col_right) VALUES (?, ?);",
            sample_rows,
        )
        connection.commit()
        print(f"Initialized database at {DB_PATH} with {len(sample_rows)} rows.")
    finally:
        connection.close()


if __name__ == "__main__":
    main()