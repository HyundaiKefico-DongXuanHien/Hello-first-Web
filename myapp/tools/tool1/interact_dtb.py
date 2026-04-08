import sqlite3

def save_issue_to_database(issue_data):
# Connect to database (creates file if not exists)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Create table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS issue_data_table (
        key TEXT PRIMARY KEY,
        request_title TEXT,
        priority TEXT,
        reporter TEXT,
        assignee TEXT,
        status TEXT,
        created TEXT,
        updated TEXT,
        due TEXT
    )
    ''')    

    cursor.execute('SELECT key FROM issue_data_table WHERE key = ?', (issue_data[0],))
    if cursor.fetchone():
        cursor.execute('''
        UPDATE issue_data_table
        SET request_title = ?, priority = ?, reporter = ?, assignee = ?, status = ?, created = ?, updated = ?, due = ?
        WHERE key = ?
        ''', (*issue_data[1:], issue_data[0]))
    else:
        cursor.execute('''
        INSERT INTO issue_data_table (key, request_title, priority, reporter, assignee, status, created, updated, due)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', issue_data)
    
    # Commit and close    
    conn.commit()
    conn.close()

def save_issue_to_database_KVHS(issue_data):
# Connect to database (creates file if not exists)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Create table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS issue_data_table_KVHS (
        key TEXT PRIMARY KEY,
        request_title TEXT,
        priority TEXT,
        reporter TEXT,
        assignee TEXT,
        status TEXT,
        created TEXT,
        updated TEXT,
        due TEXT
    )
    ''')    

    cursor.execute('SELECT key FROM issue_data_table_KVHS WHERE key = ?', (issue_data[0],))
    if cursor.fetchone():
        cursor.execute('''
        UPDATE issue_data_table_KVHS
        SET request_title = ?, priority = ?, reporter = ?, assignee = ?, status = ?, created = ?, updated = ?, due = ?
        WHERE key = ?
        ''', (*issue_data[1:], issue_data[0]))
    else:
        cursor.execute('''
        INSERT INTO issue_data_table_KVHS (key, request_title, priority, reporter, assignee, status, created, updated, due)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', issue_data)

    # Commit and close    
    conn.commit()
    conn.close()




# # Insert data
# cursor.execute('''
# INSERT INTO issue_data (key, request_title, priority, reporter, assignee, status, created, updated)
# VALUES (?, ?, ?, ?, ?, ?, ?, ?)
# ''', ('ISSUE-001', 'Fix login bug', 'High', 'Alice', 'Bob', 'Open', '2023-05-01', '2023-05-02'))

# # Query data
# cursor.execute('SELECT * FROM issue_data')
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# # Commit and close
# conn.commit()
# conn.close()

