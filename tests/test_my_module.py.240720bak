import sqlite3
import pytest
from src.my_module import perform_test

def setup_database():
    connection = sqlite3.connect(':memory:')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE test_table (
        id INTEGER PRIMARY KEY,
        input TEXT NOT NULL,
        output TEXT NOT NULL
    )
    ''')
    cursor.executemany('''
    INSERT INTO test_table (input, output) VALUES (?, ?)
    ''', [
        ('input1', 'output1'),
        ('input2', 'output2'),
        ('input3', 'output3'),
    ])
    connection.commit()
    return connection

@pytest.fixture(scope="module")
def db_connection():
    connection = setup_database()
    yield connection
    connection.close()

@pytest.fixture
def test_data(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT input, output FROM test_table")
    rows = cursor.fetchall()
    return rows

def test_database_entries(test_data):
    for input_value, expected_output in test_data:
        result = perform_test(input_value)
        assert result == expected_output
