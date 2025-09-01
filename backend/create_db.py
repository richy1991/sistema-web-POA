import sqlite3
import os

db_file = 'db.sqlite3'
schema_file = 'db_schema.sqlite'

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, db_file)
schema_path = os.path.join(script_dir, schema_file)

# Connect to the database (this will create the file if it doesn't exist)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Read the schema file
with open(schema_path, 'r') as f:
    schema = f.read()

# Execute the schema script
cursor.executescript(schema)

# Commit the changes and close the connection
conn.commit()
conn.close()

print(f"Database '{db_file}' created and schema applied successfully.")
