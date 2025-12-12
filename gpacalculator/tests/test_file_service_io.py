import pytest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fileservices import FileService

def test_write_and_read_table():
    filename = "test_table.txt"
    headers = ["ID", "Name", "Role"]
    data = [
        {"ID": "1", "Name": "Alice", "Role": "Admin"},
        {"ID": "2", "Name": "Bob", "Role": "User"},
        {"ID": "3", "Name": "Charlie", "Role": "Guest"}
    ]
    
    # 1. Write
    FileService.write_table(filename, data, headers)
    
    filepath = os.path.join(FileService.DATA_DIR, filename)
    assert os.path.exists(filepath)
    
    # Verify Content Schema
    with open(filepath, 'r') as f:
        lines = f.readlines()
        
    print("".join(lines))
    
    # Line 0: Header
    # Expected: | ID  | Name    | Role  | (approx, depends on padding)
    assert "|" in lines[0]
    assert "ID" in lines[0]
    
    # Line 1: Separator
    assert set(lines[1].strip().replace('|', '')) == {'-'}
    
    # 2. Read
    read_data = FileService.read_table(filename)
    
    assert len(read_data) == 3
    assert read_data[0]['Name'].strip() == "Alice"
    assert read_data[1]['Role'].strip() == "User"

    # Cleanup
    if os.path.exists(filepath):
        os.remove(filepath)
