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

def get_test_data():
    connection = setup_database()
    cursor = connection.cursor()
    cursor.execute("SELECT input, output FROM test_table")
    rows = cursor.fetchall()
    connection.close()
    return rows

# テストデータを取得
test_data = get_test_data()

# パラメータ化されたテスト
@pytest.mark.parametrize("input_value, expected_output", test_data)
def test_database_entries(input_value, expected_output):
    result = perform_test(input_value)
    assert result == expected_output