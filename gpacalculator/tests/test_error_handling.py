import pytest
import os
import sys
from unittest.mock import patch, mock_open

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fileservices import FileService
from students import StudentService

def test_file_service_raises_persistence_error():
    filename = "test_error.txt"
    # Mock exists to True to bypass the early return
    with patch("os.path.exists", return_value=True):
        # Mock open to raise OSError
        with patch("builtins.open", side_effect=OSError("Access denied")):
            with pytest.raises(OSError):
                FileService.read_table(filename)

def test_student_service_handles_persistence_error(capsys):
    """Verify that StudentService catches error, rolls back, and re-raises."""
    
    # We mock FileService.write_table to raise OSError
    with patch("fileservices.FileService.write_table", side_effect=OSError("Disk full")):
        
        # Expect OSError to bubble up
        with pytest.raises(OSError):
             StudentService.create_student("ERR_S01", "Error Student")
        
        # Verify rollback (List should be clean of this student)
        found = any(s['id'] == "ERR_S01" for s in StudentService.students)
        assert not found, "Student should have been removed from list on failure"
